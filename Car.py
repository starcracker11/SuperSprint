import GameMob
import Point
import Polygon as polygonLib

class Car(GameMob.GameMob):
    def __init__(self, width, height, max_speed, max_acceleration, weight, friction, colour):
        super(Car, self).__init__(width, height, max_speed, max_acceleration, weight, friction, colour)

        # we can make the car out of several polygons in the future but for now it's a rectangle
        # for now it's width and height can be sert from this existing class proeprties
        tmp_car_points = [(0, 0), (self.width, 0), (self.width, self.height), (0, self.height)]
        self.car_polygons = []
        self.car_polygons.append(polygonLib.Polygon(tmp_car_points))
        self.angle = 90
        self.position = Point.Point(328, 78)

    def get_polygons(self):
        return self.car_polygons
