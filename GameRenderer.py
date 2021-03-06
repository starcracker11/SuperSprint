import pygame
import CarGame as carGameLib
import BaseRenderer as baseRenderer
import TextRenderer as textLib
import copy

class GameRenderer(baseRenderer.BaseRenderer):
    def __init__(self, car_game, screen):
        super().__init__(screen)
        self.car_game = car_game
        self.lap_text_renderer = textLib.TextRenderer(screen)
        self.lap_text_renderer.scale = 0.2

    def render(self):
        # clear screen:
        self.screen.fill((0, 100, 0))

        self.lap_text_renderer.render_text(self.car_game.users[0].name + " LAP " +
                                           str(self.car_game.users[0].get_lap_counter()), 10, 10)

        if len(self.car_game.users) > 1:
            self.lap_text_renderer.render_text(self.car_game.users[1].name + " LAP " +
                                           str(self.car_game.users[1].get_lap_counter()), 500, 10)

        # loop through track polygons and draw them
        for poly in self.car_game.track.polygons:
            self.render_polygon(poly)

        # loop through track markers so we can see what's going on
        for track_marker in self.car_game.track.track_markers:
            line = track_marker.line
            self.render_line(line)

        # now render all the cars
        for user in self.car_game.users:
            for poly in user.car.car_polygons:
                self.render_polygon(poly, user.car.position.x, user.car.position.y, user.car.colour)

            # hack in our sweep lines
            car_line = user.car.get_collision_line()
            tmp_line = copy.copy(car_line)

            # left hand aI areas
            tmp_line.point_2 = car_line.point_2.rotate(-45, car_line.point_1.x, car_line.point_1.y)
            self.render_line(tmp_line, user.car.position.x, user.car.position.y)

            # right hand aI areas
            tmp_line.point_2 = car_line.point_2.rotate(45, car_line.point_1.x, car_line.point_1.y)
            self.render_line(tmp_line, user.car.position.x, user.car.position.y)


