import pygame

class BaseRenderer:

    def __init__(self, screen):
        self.screen = screen
        self.scale = 1.35

    def render_line(self, line, offset_x=0, offset_y=0):
        pygame.draw.line(self.screen, line.colour,
                         (line.point_1.x * self.scale + offset_x, line.point_1.y * self.scale + offset_y),
                         (line.point_2.x * self.scale + offset_x, line.point_2.y * self.scale + offset_y))

    def render_polygon(self, poly, offset_x=0, offset_y=0, colour=(0, 0, 0)):
        for line in poly.lines:
            pygame.draw.line(self.screen, line.colour, ((line.point_1.x + offset_x) * self.scale,
                                                        (line.point_1.y + offset_y) * self.scale),
                             ((line.point_2.x + offset_x) * self.scale, (line.point_2.y + offset_y) * self.scale))