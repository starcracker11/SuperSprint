import Point as pointLib


class Polygon(object):
    def __init__(self, points=[]):
        self.points = []
        self.set_points_from_tuples(points)
        print("created polygon with points: " + str(len(self.points)))

    def get_points(self):
        return self.points

    def set_points(self, array):
        self.points = array

    def set_points_from_tuples(self, points=[]):
        self.points = []
        for tmp_tuple in points:
            self.points.append(pointLib.Point(tmp_tuple[0], tmp_tuple[1]))