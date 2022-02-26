import pygame
import CarGame as carGameLib
import BaseRenderer as baseRenderer
import TextRenderer as textLib


class GameRenderer(baseRenderer.BaseRenderer):
    def __init__(self, car_game, screen):
        super().__init__(screen)
        self.car_game = car_game
        self.lap_text_renderer = textLib.TextRenderer(screen)
        self.lap_text_renderer.scale = 0.2

    def render(self):
        self.lap_text_renderer.render_text("LAP ", 10, 10)
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


