import math

import TextRenderer as textLib


class TitleScreenRenderer(textLib.TextRenderer):
    def __init__(self, screen):
        super().__init__(screen)
        self.scale = 0.85
        self.wobble = 0
        self.counter = 0

    def render(self):
        # darw titl of game
        x_offset = 1024/2 - 300
        offset_y = 40
        small_line_gap = self.scale*120
        self.render_text("car game", x_offset, offset_y)
        offset_y += small_line_gap
        self.render_text("Press Space", x_offset-100, offset_y)
        offset_y += small_line_gap
        self.render_text("To Start", x_offset, offset_y)


    def update(self):
        self.counter += 1
        self.scale = 0.75 # + 0.01*math.sin(math.radians(self.counter*2))
        # self.wobble = 5*math.sin(math.radians(self.counter*2))
