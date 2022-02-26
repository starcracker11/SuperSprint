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
        tmp_car_polygon = polygonLib.Polygon(tmp_car_points)
        self.car_polygons.append(tmp_car_polygon)
        self.position = Point.Point(328, 78)
        self.acceleration = 0
        self.max_acceleration = 20
        self.max_velocity = 2
        # add a collision line 'polygon' that we can test for incoming collisions
        self.collision_line = polygonLib.Polygon([(self.width/2, self.height/2), (self.width/2, self.height+self.height/2)])
        self.car_polygons.append(self.collision_line)

        # THIS IS NOT GOOD BOTH ACCELERATION AND VELOCITY SHOULD BE VECTORS
        self.velocity = Point.Point(0, 0)
        self.angle = 0

        # finally, reposition all the polygons so they're facing the right way
        # this angle of direction will be loaded from a track object
        # and set:
        self.set_angle(270 * 1000)

    def get_polygons(self):
        return self.car_polygons

    def increase_acceleration(self):
        self.acceleration += 0.125
        if self.acceleration > self.max_acceleration:
            self.acceleration = self.max_acceleration

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
        self.velocity.x -= (self.velocity.x/100)
        self.velocity.y -= (self.velocity.y/100)

    def get_angle(self):
        return self.angle

    def increase_turn_angle(self, value=2):
        self.set_angle(self.angle+value)

    def decrease_turn_angle(self, value=2):
        self.set_angle(self.angle-value)

    # this updates the 'rotated points' of any polygons
    def set_angle(self, angle):
        self.angle = angle
        # now update points in polygons
        for poly in self.car_polygons:
            poly.set_angle(self.angle, self.width/2, self.height/2)


