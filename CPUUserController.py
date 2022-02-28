import Track
import User
import copy
import math
import Point
import Line
import Polygon as polygonLib


def get_angle_to_marker(track, current_marker, x_point, y_point):
    if current_marker.index == 2:
        # we're on the last one, so look for first:
        track_marker_to_head_towards = track.ending_line_track_marker
    else:
        track_marker_to_head_towards = track.track_markers[current_marker.index + 1]
    # find direction of car to marker
    p1 = current_marker.line.point_1

    # from website: https://www.mathworks.com/matlabcentral/answers/519236-finding-angle-between-2-points
    # r1 = sqrt((x1 - xo). ^ 2 + (y1 - yo). ^ 2);
    # r2 = sqrt((x2 - xo). ^ 2 + (y2 - yo). ^ 2);
    # alpha = acos((x1 - xo) / r1);
    # beta = acos((x2 - xo) / r2);
    # theta = alpha - beta;
    #xo = yo = 0
    x1 = x_point
    y1 = y_point
    x2 = track_marker_to_head_towards.line.point_1.x
    y2 = track_marker_to_head_towards.line.point_1.y#

    #r1 = math.sqrt(math.pow(x1 - xo, 2) + math.pow(y1 - yo, 2))
    #r2 = math.sqrt(math.pow(x2 - xo, 2) + math.pow(y2 - yo, 2))
    #alpha = math.acos((x1 - xo) / r1)
    #if r2 == 0:
    #    r2 = 0.1
    #beta = math.acos((x2 - x1) / r2)
    #theta = alpha - beta

    #arc_tan = math.atan2(y_point - p1.y, x_point - p1.x)
    #print('angle to marker: ' + str(math.degrees(alpha)) + ", " + str(math.degrees(beta)) + ", " + str(math.degrees(theta)))

    # https://blog.finxter.com/calculating-the-angle-clockwise-between-2-points/
    v1_theta = math.atan2(y1, x1)
    v2_theta = math.atan2(y2, x2)
    r = (v2_theta - v1_theta) * (180.0 / math.pi)
    if r < 0:
        r % 360
    print('angle:'  + str(r) + "points: " + str(x1)+","+str(y1)+" --- " + str(x2)+","+str(y2))


class CPUUserController(User.User):
    def __init__(self, name, colour):
        super().__init__(name, colour)
        # now update its collision line so it's much longer
        self.car.collision_line.lines[0].point_1.y = 80
        self.car.max_velocity = self.car.max_velocity / 2
        self.car.max_acceleration = self.car.max_acceleration
        # hack in correct angle
        self.car.set_angle(270)

    def update_state(self, track):
        # accelerate, turn, brake depending on obstacles

        collision_angle_left_angle_inner_sweep = 0
        collision_angle_right_angle_inner_sweep = 0
        collision_angle_left_angle_outer_sweep = 0
        collision_angle_right_angle_outer_sweep = 0
        tmp_collision_left_line = None
        tmp_collision_right_line = None
        steer_direction = 0
        LEFT = 2
        RIGHT = -2
        direction_found = False
        car_line = self.car.get_collision_line()
        tmp_line = copy.copy(car_line)
        # need to determine if there's a collision coming up:
        for poly in track.polygons:
            if steer_direction != 0:
                break
            for track_line in poly.lines:
                # this can be removed once everything is working
                track_line.set_collision_flag(False)

                # try and find the middle of the road
                # so instead of sweep left to right, wel'' sweep center outwards
                for sweep_angle in range(0, 45):
                    # sweep right
                    if tmp_collision_right_line is None and steer_direction == 0:
                        tmp_line.point_2 = car_line.point_2.rotate(sweep_angle, car_line.point_1.x, car_line.point_1.y)
                        if track_line.check_intersect(tmp_line, self.car.position.x, self.car.position.y):
                            collision_angle_right_angle_inner_sweep = sweep_angle
                            tmp_collision_right_line = track_line
                            steer_direction = LEFT

                    # sweep left
                    if tmp_collision_left_line is None and steer_direction == 0:
                        tmp_line.point_2 = car_line.point_2.rotate(-sweep_angle, car_line.point_1.x, car_line.point_1.y)
                        if track_line.check_intersect(tmp_line, self.car.position.x, self.car.position.y):
                            collision_angle_left_angle_inner_sweep = -sweep_angle
                            steer_direction = RIGHT
                            tmp_collision_left_line = track_line

                if tmp_collision_left_line is not None or tmp_collision_right_line is not None:
                    # we have found a potential collision, so determine which direction to go AWAY FROM it
                    big_sweep = 45
                    collision_angle_left_angle_outer_sweep = big_sweep
                    collision_angle_right_angle_outer_sweep = big_sweep
                    tmp_collision_right_line = None
                    tmp_collision_left_line = None
                    # this indicates the sweep didn't have time to start moving
                    # so sweep inwards to see what side has the bigger gap
                    for sweep_angle in range(0, big_sweep):

                        # sweep right
                        if tmp_collision_left_line is None:
                            tmp_line.point_2 = car_line.point_2.rotate(-big_sweep - sweep_angle, car_line.point_1.x,
                                                                       car_line.point_1.y)
                            if track_line.check_intersect(tmp_line, self.car.position.x, self.car.position.y):
                                collision_angle_left_angle_outer_sweep = -big_sweep - sweep_angle
                                tmp_collision_left_line = track_line

                        # sweep left
                        if tmp_collision_right_line is None:
                            tmp_line.point_2 = car_line.point_2.rotate(big_sweep - sweep_angle, car_line.point_1.x,
                                                                       car_line.point_1.y)
                            if track_line.check_intersect(tmp_line, self.car.position.x, self.car.position.y):
                                collision_angle_right_angle_outer_sweep = big_sweep - sweep_angle
                                tmp_collision_right_line = track_line

                    if tmp_collision_right_line is not None and tmp_collision_left_line is not None:
                        print('AI: dont know what to do here')
                    if tmp_collision_right_line is not None:
                        steer_direction = LEFT
                    elif tmp_collision_left_line is not None:
                        steer_direction = RIGHT

        if steer_direction == 0:
            # so we're keeping on going same direction?
            # let's try and head towards the next track_marker instead
            track_marker_to_head_towards = None
            get_angle_to_marker(track, self.current_track_marker, self.car.position.x, self.car.position.y)
            self.car.increase_acceleration()
        else:
            self.car.increase_acceleration()
            if steer_direction == LEFT:
                self.car.turn_left()
            elif steer_direction == RIGHT:
                self.car.turn_right()

        super().update_state(track)
