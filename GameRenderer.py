import pygame
import CarGame as carGameLib


class GameRenderer:
    def __init__(self, car_game, screen):
        self.car_game = car_game
        self.screen = screen

    def render_game(self):
        # loop through track polygons and draw them
        for poly in self.car_game.track.polygons:
            self.render_polygon(poly)

        # now render all the cars
        for user in self.car_game.users:
            for poly in user.car.car_polygons:
                # print("rendering car at " + str(user.car.position.x) + ", " + str(user.car.position.y))
                self.render_polygon(poly, user.car.position.x, user.car.position.y, user.car.colour, user.car.angle)

    def render_polygon(self, poly, offset_x=0, offset_y=0, colour=(0, 0, 0), angle=0):
        # for now all lines will be black
        # in the future we need a more detailed class that contains a Polygon object
        # and data about the 'game object' like colour/texture
        tmp_polygon_points = poly.get_points()
        # print(" polygon points read from track: " + str(len(tmp_polygon_points)))
        for index, pointItem in enumerate(tmp_polygon_points):
            point = pointItem.rotate(angle, 0, 0)
            # if index is less than max, then join to next point
            # otherwise join to first point
            if index > len(tmp_polygon_points) - 2:
                first_point = tmp_polygon_points[0]
                pygame.draw.line(self.screen, colour, (point.x + offset_x, point.y + offset_y),
                                 (first_point.x + offset_x, first_point.y + offset_y))
            elif index < len(tmp_polygon_points) - 1:
                next_point = tmp_polygon_points[index + 1]
                pygame.draw.line(self.screen, colour, (point.x + offset_x, point.y + offset_y),
                                 (next_point.x + offset_x, next_point.y + offset_y))


