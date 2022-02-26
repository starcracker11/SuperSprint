import Point as pointLib
import Line as lineLib
import copy


class Polygon(object):
    def __init__(self, points=[]):
        self.points = []
        self.lines = []
        self.untouched_Points = []
        self.set_points_from_tuples(points)
        self.convert_points_into_lines(self.points)
        self.angle = 0
        print("created polygon with points: " + str(len(self.points)))

    def get_points(self):
        return self.points

    def set_points(self, array):
        self.points = array
        self.untouched_Points = copy.copy(self.points)

    def set_points_from_tuples(self, points=[]):
        self.points = []
        for tmp_tuple in points:
            self.points.append(pointLib.Point(tmp_tuple[0], tmp_tuple[1]))
        self.untouched_Points = copy.copy(self.points)

    def set_angle(self, angle, center_x, center_y):
        self.angle = angle
        self.points = []
        for point in self.untouched_Points:
            self.points.append(point.rotate(-angle, center_x, center_y))
        self.convert_points_into_lines(self.points)

    def convert_points_into_lines(self, points=[]):
        self.lines = []
        for index, pointItem in enumerate(self.points):
            point = pointItem
            # if index is less than max, then join to next point
            # otherwise join to first point
            if index > len(self.points) - 2:
                first_point = self.points[0]
                self.lines.append(lineLib.Line(first_point, point))
            elif index < len(self.points) - 1:
                next_point = self.points[index + 1]
                self.lines.append(lineLib.Line(next_point, point))

    # this tests for a collision between this Polygon
    # and another polygon that is passed
#  def test_for_collision(self, polygon):
#      for point in self.points:
#          tmpPoint = point
# we need to got through each point and line with every one in the given Polygon
