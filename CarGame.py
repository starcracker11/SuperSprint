import math

import Track as trackLib
import User as userLib
import CPUUserController as cpuUSer


class CarGame(object):
    def __init__(self):
        self.track = trackLib.Track()
        self.users = []
        # self.users = [userLib.User('PLAYER 1', (200, 200, 0)),
        #              userLib.User('PLAYER 2', (0, 0, 200))]

        self.users.append(userLib.User('PLAYER 1', (200, 200, 0)))
        self.users.append(cpuUSer.CPUUserController('CPU 1', (0, 100, 150)))
        # self.users.append(cpuUSer.CPUUserController('CPU 2', (0, 100, 150)))
        # self.users.append(cpuUSer.CPUUserController('CPU2', (50, 100, 150)))

        self.winning_user = userLib.User

    # reposition users at stat of track
    def reset(self):
        self.winning_user = None
        starting_line = self.track.get_starting_line()
        # TODO: using y = mx + c we might be able to find point along the starting_line
        tmp_y_shift = starting_line.line.point_1.y + 40
        for user in self.users:
            # TODO: center the cars so they appear in a row along the starting line
            user.car.position.x = starting_line.line.point_1.x
            user.car.position.y = tmp_y_shift
            user.set_track_marker(starting_line)
            user.reset_lap_counter()
            tmp_y_shift += 20

    def is_game_over(self):
        return self.winning_user is not None

    def update(self):
        cpuUSer.get_angle_to_marker(self.track, self.users[0].current_track_marker, self.users[0].car.position.x, self.users[0].car.position.y)
        # print('angle: ' + str(self.users[0].car.angle))
        # self.track.update()
        for user in self.users:
            # we now need to determine if a car has reached a track-marker
            for track_marker in self.track.track_markers:
                if track_marker.line.check_intersect(user.car.collision_line.lines[0], user.car.position.x,
                                                     user.car.position.y):
                    # it collided with a marker, so we need logic to determine
                    # if this is the correct 'next' marker that needed hitting
                    # so, let's store marker index on user (or the car? ...no, user)

                    # first check if this line is the start/finish line
                    if track_marker == self.track.track_markers[0]:
                        # it is but have we ever left it?
                        # we could have marked this last one if we had passed the second one
                        if user.get_track_marker() == self.track.get_ending_line():
                            print("CURCUIT COMPLETE")
                            # so just reset the users current marker...
                            # TODO: maybe increment a lap counter
                            # TODO: determine max imum nuber of laps reached and gave over screen
                            user.increment_lap_counter()
                            user.set_track_marker(track_marker)
                            if user.get_lap_counter() == self.track.max_laps:
                                self.winning_user = user

                    # now _only_ set the user with a new 'current track marker' on a few conditions:
                    if user.get_track_marker().index == track_marker.index - 1 \
                            or user.get_track_marker().index == track_marker.index + 1:
                        user.set_track_marker(track_marker)

            # check for collision
            for poly in self.track.polygons:
                for track_line in poly.lines:
                    # this can be removed once everything is working
                    track_line.set_collision_flag(False)
                    # we could use the collision_line to work out the angle of incidence (bounce angle)
                    car_line = user.car.collision_line.lines[0]
                    for car_line in user.car.car_polygons[0].lines:
                        if track_line.check_intersect(car_line, user.car.position.x, user.car.position.y):
                            self.handle_car_collision(track_line, user)

            user.update_state(self.track)

            # debug only: show crossed state for player 1
            for track_marker in self.track.track_markers:
                track_marker.line.colour = (0, 0, 0)
            player1 = self.users[0]
            player1.current_track_marker.line.colour = (0, 255, 0)

    def handle_car_collision(self, track_line, user):
        # this means we have a collision
        track_line.set_collision_flag(True)
        # user.car.acceleration = 0
        # instead of stopping velocity, instead
        # ...calculate the angle of incidence in order o 'bounce' off the sides
        # I used this formula: https://byjus.com/maths/angle-between-two-lines/
        m1 = track_line.get_slope()
        m2 = user.car.collision_line.lines[0].get_slope()
        tan_theta = (m1 - m2) / (1 + m1 * m2)
        theta = math.atan(tan_theta)
        angle_reflection_radians = math.radians(90) - theta
        # NEED TO WORK OUT ANGLE TO MAKE CAR FACE MAYBE?
        # user.car.set_angle(-math.degrees(theta*1000))
        # OR JUST ALTER VELOCITY
        # print("collision theta: " + str(math.degrees(theta)))
        # if math.degrees(theta) < 40:
        #    user.car.increase_turn_angle(-math.degrees(theta))
        # else:
        user.car.velocity.x = user.car.velocity.x / 3
        user.car.velocity.y = user.car.velocity.y / 3
        # user.car.set_angle(math.radians(angle_reflection_radians) * 1000wd)
        user.car.velocity.x = 2 * user.car.velocity.x * math.cos(
            angle_reflection_radians) - 2 * user.car.velocity.x * math.sin(
            angle_reflection_radians)
        user.car.velocity.y = 2 * user.car.velocity.y * math.cos(
            angle_reflection_radians) + 2 * user.car.velocity.y * math.sin(
            angle_reflection_radians)
        # user.car.velocity.x = 2*user.car.velocity.x*math.sin(angle_reflection_degress) - 2*user.car.velocity.x*math.cos(angle_reflection_degress)
        # user.car.velocity.y = 2*user.car.velocity.y*math.cos(angle_reflection_degress) + 2*user.car.velocity.y*math.sin(angle_reflection_degress)
        # user.car.velocity.x = 2*user.car.velocity.x*math.sin(theta) - 2*user.car.velocity.x*math.cos(theta)
        # user.car.velocity.y = 2*user.car.velocity.y*math.cos(theta) + 2*user.car.velocity.y*math.sin(theta)
        # user.car.velocity.x = -2*user.car.velocity.x * math.cos(math.radians(user.car.get_angle()))
        # user.car.velocity.y = -2*user.car.velocity.y * math.sin(math.radians(user.car.get_angle()))
