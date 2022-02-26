import math

import Track as trackLib
import User as userLib


class CarGame(object):
    def __init__(self):
        self.track = trackLib.Track()
        self.users = [userLib.User('PLAYER 1', (255, 0, 0)),
                      userLib.User('PLAYER 2', (0, 255, 0))]
        self.winning_user = userLib.User

    # reposition users at stat of track
    def reset(self):
        self.winning_user = None
        for user in self.users:
            # TODO: center the cars so they appear in a row along the starting line
            user.car.position.x = self.track.starting_line_track_marker.line.point_1.x
            user.car.position.y = self.track.starting_line_track_marker.line.point_1.y
            user.set_track_marker(self.track.starting_line_track_marker)
            user.reset_lap_counter()

    def is_game_over(self):
        return self.winning_user is not None

    def update(self):
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
                        if user.get_track_marker() == self.track.ending_line_track_marker:
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

            user.car.update_state()

            # check for collision
            # loop through each user
            for poly in self.track.polygons:
                for track_line in poly.lines:
                    track_line.set_collision_flag(False)
                    for user in self.users:
                        # we could use the collision_line to work out the angle of incidence (bounce angle)
                        car_line = user.car.collision_line.lines[0]
                        for car_line in user.car.car_polygons[0].lines:
                            # if True:
                            if track_line.check_intersect(car_line, user.car.position.x, user.car.position.y):
                                self.handle_car_collision(track_line, user)

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
