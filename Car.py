import math

import GameMob
import Point
import Polygon as polygonLib


class Car(GameMob.GameMob):
    def __init__(self, width, height, max_speed, max_acceleration, weight, friction, colour):
        super(Car, self).__init__(width, height, max_speed, max_acceleration, weight, friction, colour)

        # we can make the car out of several polygons in the future but for now it's a rectangle
        # for now it's width and height can be sert from this existing class proeprties
        # tmp_car_points = [(0, 0), (self.width, 0), (self.width, self.height), (0, self.height)]
        tmp_car_points = [(0, 0), (self.width, 0), (self.width, self.height), (0, self.height)]
        self.car_polygons = []
        self.car_polygons.append(polygonLib.Polygon(tmp_car_points, colour))
        self.position = Point.Point(328, 78)
        self.acceleration = 0
        self.max_acceleration = 20
        self.max_velocity = 2
        # add a collision line 'polygon' that we can test for incoming collisions
        self.collision_line = polygonLib.Polygon([(self.width/2, self.height/2), (self.width/2, self.height+self.height*3)])
        self.car_polygons.append(self.collision_line)
        self.brake = False

        # THIS IS NOT GOOD BOTH ACCELERATION AND VELOCITY SHOULD BE VECTORS
        self.velocity = Point.Point(0, 0)
        self.angle = 0

        # finally, reposition all the polygons so they're facing the right way
        # this angle of direction will be loaded from a track object
        # and set:
        self.set_angle(90)

    def get_polygons(self):
        return self.car_polygons

    def increase_acceleration(self):
        self.acceleration += 0.125
        if self.acceleration > self.max_acceleration:
            self.acceleration = self.max_acceleration

    def hit_brake(self):
        self.brake = True

    # really this is zero acceleration and just movement due to momentum
    # this should vary depending on the surface
    def stop_acceleration(self):
        self.acceleration = 0

    # this changes the position based on direction and speed
    # if a collision happens then this can be checked in CarGame as it has the track
    # so a simple translation based on direction and speed?
    def update_state(self):

        # THIS IS NOT GOOD BOTH ACCELERATION AND VELOCITY SHOULD BE VECTORS
        self.velocity.x += (self.acceleration/100 * math.sin(math.radians(self.get_angle())))
        self.velocity.y += (self.acceleration/100 * math.cos(math.radians(self.get_angle())))

        if self.velocity.x > 0 and self.velocity.x > self.max_velocity:
            self.velocity.x = self.max_velocity
        elif self.velocity.x < 0 and self.velocity.x < -self.max_velocity:
            self.velocity.x = -self.max_velocity

        if self.velocity.y > 0 and self.velocity.y > self.max_velocity:
            self.velocity.y = self.max_velocity
        elif self.velocity.y < 0 and self.velocity.y < -self.max_velocity:
            self.velocity.y = -self.max_velocity;

        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        # slowdown due to friction:
        # THIS IS NOT GOOD BOTH ACCELERATION AND VELOCITY SHOULD BE VECTORS
        slow_amount = 100
        if self.brake:
            slow_amount = 2

        self.velocity.x -= (self.velocity.x/slow_amount)
        self.velocity.y -= (self.velocity.y/slow_amount)

    def get_angle(self):
        return self.angle

    def turn_left(self, value=2):
        self.set_angle(self.angle+value)

    def turn_right(self, value=2):
        self.set_angle(self.angle-value)

    # TODO: This is terribly hack but the problems stem from precision loss in rotations
    def get_collision_line(self):
        tmp_last_poly = self.car_polygons[len(self.car_polygons)-1]
        return tmp_last_poly.lines[len(tmp_last_poly.lines)-1]

    # this updates the 'rotated points' of any polygons
    def set_angle(self, angle):
        self.angle = angle % 360
        # now update points in polygons
        for poly in self.car_polygons:
            poly.set_angle(self.angle, self.width/2, self.height/2)




