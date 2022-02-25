import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, angle, cx, cy):
        if not angle == 0:
            tmp_x = self.x
            tmp_y = self.y
            sin_tmp = math.sin(math.radians(angle))
            cos_tmp = math.cos(math.radians(angle))

            # translate point back to origin:
            tmp_x -= cx
            tmp_y -= cy

            # rotate point
            x_new = tmp_x * cos_tmp - tmp_y * sin_tmp
            y_new = tmp_x * sin_tmp + tmp_y * cos_tmp

            # translate point back:
            tmp_x = x_new + cx
            tmp_y = y_new + cy

            return Point(tmp_x, tmp_y)
        else:
            return self
