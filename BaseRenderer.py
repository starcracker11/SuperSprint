import math

import pygame

import Line
import Point
import Polygon as polyLib

class BaseRenderer:

    def __init__(self, screen):
        self.screen = screen
        self.scale = 1

    def render_line(self, line, offset_x=0, offset_y=0):
        pygame.draw.line(self.screen, line.colour,
                         (line.point_1.x * self.scale + offset_x, line.point_1.y * self.scale + offset_y),
                         (line.point_2.x * self.scale + offset_x, line.point_2.y * self.scale + offset_y), math.ceil(1*self.scale))

    def render_polygon(self, poly=polyLib.Polygon, offset_x=0, offset_y=0, colour=(0, 0, 0)):
        tmp_list = poly.get_points_as_tuples(offset_x, offset_y, self.scale)
        if len(poly.get_points()) > 2:
            pygame.draw.polygon(self.screen, poly.colour, tmp_list)
        else:
            # must be a line
            self.render_line(Line.Line(Point.Point(tmp_list[0][0], tmp_list[0][1]), Point.Point(tmp_list[1][0], tmp_list[1][1])))
        #for line in poly.lines:
        #    pygame.draw.line(self.screen, line.colour, ((line.point_1.x + offset_x) * self.scale,
        #                                                (line.point_1.y + offset_y) * self.scale),
        #                     ((line.point_2.x + offset_x) * self.scale, (line.point_2.y + offset_y) * self.scale))