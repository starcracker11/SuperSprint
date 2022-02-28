import Point as pointLib
import copy


def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise

    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/
    # for details of below formula.

    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if val > 0:
        # clockwise orientation
        return 1

    elif val < 0:
        # Counterclockwise orientation
        return 2
    else:
        # Collinear orientation
        return 0


class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        self.colour = (0, 0, 0)
        self.collision_flag = False

    def set_collision_flag(self, value):
        self.collision_flag = value
        if self.collision_flag:
            self.colour = (255, 0, 0)
        else:
            self.colour = (0, 0, 0)

    # this is quite complicated BUT this website explains it perfectly:
    # https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
    def check_intersect(self, line, offset_x, offset_y):
        return_val = False
        # this is done because we keep the car polygon's co-ordinates from a fixed reference point
        # due to potential loss of precision loss with rotations
        line.point_1.x += offset_x
        line.point_2.x += offset_x
        line.point_1.y += offset_y
        line.point_2.y += offset_y

        o1 = orientation(self.point_1, self.point_2, line.point_1)
        o2 = orientation(self.point_1, self.point_2, line.point_2)
        o3 = orientation(line.point_1, line.point_2, self.point_1)
        o4 = orientation(line.point_1, line.point_2, self.point_2)

        # General case
        if (o1 != o2) and (o3 != o4):
            return_val = True

        # Special Cases
        if (o1 == 0) and self.on_segment(self.point_1, line.point_1, self.point_2):
            # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
            return_val = True
        elif (o2 == 0) and self.on_segment(self.point_1, line.point_2, self.point_2):
            # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
            return_val = True
        elif (o3 == 0) and self.on_segment(line.point_1, self.point_2, line.point_2):
            # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
            return_val = True
        elif (o4 == 0) and self.on_segment(line.point_1, self.point_2, line.point_2):
            # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
            return_val = True

        line.point_1.x -= offset_x
        line.point_2.x -= offset_x
        line.point_1.y -= offset_y
        line.point_2.y -= offset_y
        return return_val

    def on_segment(self, p, q, r):
        if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
                (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
            return True
        return False

    def get_slope(self):
        top = 0
        bottom = 0
        if self.point_1.x > self.point_2.x:
            bottom = self.point_1.x - self.point_2.x
        else:
            bottom = self.point_2.x - self.point_1.x

        if self.point_1.y > self.point_2.y:
            top = self.point_1.y - self.point_2.y
        else:
            top = self.point_2.y - self.point_1.y
        if bottom > 0:
            return top / bottom
        else:
            return 0

    def get_points_as_tuples(self):
        return [ (self.point_1.x, self.point_1.y), (self.point_2.x, self.point_2.y) ]