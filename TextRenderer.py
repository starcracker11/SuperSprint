import Line
import VectorCharacter as charLib
import Point as pointLib
import BaseRenderer as baseRenderer


# this class contains code to render text to screen
# using vectors/lines. However, there's no time left to generate this data
# for every 26 + 10 letters and numbers
class TextRenderer(baseRenderer.BaseRenderer):
    def __init__(self, screen):
        super().__init__(screen)
        self.car_game_title = []
        self.characters = []
        self.raw_vector_data = []
        self.load_raw_vector_data()
        self.y_line_offset = 0

    def load_raw_vector_data(self):
        for raw_data_char in raw_data:
            self.raw_vector_data_append(raw_data_char)

    # loads an individual chunk of line data for a character
    def raw_vector_data_append(self, char_data):
        new_lines = []
        for item in char_data:
            new_lines.append(Line.Line(pointLib.Point(item[0][0], item[0][1]),
                                       pointLib.Point(item[1][0], item[1][1])))

        self.characters.append(charLib.VectorCharacter(new_lines))

    def get_vector_object_for_char(self, required_char):
        # get ASCII value of character
        # find correct position in list of characters
        # 'A' starts at 65 in the character set, so offset required char with that
        as_ascii = ord(required_char)
        if as_ascii - 65 >= 0:
            return self.characters[as_ascii - 65]
        else:
            return None

    def render_text(self, msg, offset_x=0, offset_y=0):
        start_position_x = offset_x
        font_gap = (w + w / 2 + w / 3) * self.scale
        for c in msg:
            vector_char = self.get_vector_object_for_char(c)
            if vector_char is not None:
                for line in vector_char.lines:
                    self.render_line(line, start_position_x, self.y_line_offset + offset_y)
            start_position_x += font_gap

    def render(self):
        self.y_line_offset = 100
        self.render_text("PLAYER ONE")
        self.y_line_offset += 150
        self.render_text("  WON")
        # self.y_line_offset += 150
        # self.render_text("WXYZ")

# this is all point data for character set
w = 50
h = 100
raw_data = [
    # char A
    [((w / 2, 0), (0, h / 5)),
     ((0, h / 5), (0, h)),
     ((w, h / 5), (w, h)),
     ((w / 2, 0), (w, h / 5)),
     ((0, h - h / 5), (w, h - h / 5))
     ],
    # char B
    [((0, 0), (w / 2, 0)),
     ((w / 2, 0), (w, h / 3)),
     ((w, h / 3), (w / 2, h / 2)),
     ((w / 2, h / 2), (w, 2 * (h / 3))),
     ((w, 2 * (h / 3)), (w / 2, h)),
     ((w / 2, h), (0, h)),
     ((0, 0), (0, h)),
     ((w / 2, h / 2), (0, h / 2))
     ],
    # char C
    [((0, 0), (w, 0)),
     ((0, 0), (0, h)),
     ((0, h), (w, h))
     ],
    # char D
    [((0, 0), (0, h)),
     ((0, 0), (w / 3, 0)),
     ((w / 3, 0), (w, h / 4)),
     ((w, h / 4), (w, 3 * (h / 4))),
     ((w, 3 * (h / 4)), (w / 3, h)),
     ((w / 3, h), (0, h))
     ],
    # char E
    [((0, 0), (w, 0)),
     ((0, 0), (0, h)),
     ((0, h), (w, h)),
     ((0, h / 2), (w / 2, h / 2))
     ],
    # char F
    [((0, 0), (w, 0)),
     ((0, 0), (0, h)),
     ((0, h / 2), (w / 2, h / 2))
     ],
    # char G
    [((0, 0), (w, 0)),
     ((0, 0), (0, h)),
     ((0, h), (w, h)),
     ((w, h / 2), (w, h)),
     ((w, h / 2), (w / 2, h / 2))
     ],
    # char H
    [((0, 0), (0, h)),
     ((w, 0), (w, h)),
     ((0, h / 2), (w, h / 2))
     ],
    # char I
    [((w / 4, 0), (w / 2 + w / 4, 0)),
     ((w / 2, 0), (w / 2, h)),
     ((w / 4, h), (w / 2 + w / 4, h))
     ],
    # char J
    [((w, 0), (w, h)),
     ((w, h), (w/2, h)),
     ((w/2, h), (0, h/2+h/4))],
    # char K
    [((0, 0), (0, h)),
     ((0, h/2), (w, 0)),
     ((0, h/2), (w, h))
     ],
    # char L
    [((0, 0), (0, h)),
     ((0, h), (w, h))
     ],
    # char M
    [((0, 0), (0, h)),
     ((0, 0), (w/2, h/4)),
     ((w, 0), (w/2, h/4)),
     ((w, 0), (w, h))],
    # char N
    [((0, 0), (0, h)),
     ((w, 0), (w, h)),
     ((0, 0), (w, h))
    ],
    # char O
    [((0, 0), (w, 0)),
     ((0, 0), (0, h)),
     ((0, h), (w, h)),
     ((w, 0), (w, h))],
    # char P
    [((0, 0), (w, 0)),
     ((0, 0), (0, h)),
     ((0, h/2), (w, h/2)),
     ((w, 0), (w, h/2))],
    # char Q
    [((0, 0), (w, 0)),
     ((0, 0), (0, h)),
     ((0, h), (w/2, h)),
     ((w/2, h), (w, h-h/5)),
     ((w, 0), (w, h-h/5)),
     ((w, h), (w/2, h-h/5)),
     ],
    # char R
    [((0, 0), (w, 0)),
     ((0, 0), (0, h)),
     ((0, h/2), (w, h/2)),
     ((w, 0), (w, h/2)),
     ((0, h/2), (w, h))],
    # char S
    [((0, 0), (w, 0)),
     ((0, 0), (0, h/2)),
     ((0, h/2), (w, h/2)),
     ((w, h/2), (w, h)),
     ((0, h), (w, h))],
    # char T
    [((w / 4, 0), (w / 2 + w / 4, 0)),
     ((w / 2, 0), (w / 2, h))],
    # char U
    [((0, 0), (0, h)),
     ((0, h), (w, h)),
     ((w, 0), (w, h))],
    # char V
    [((0, 0), (w/2, h)),
     ((w/2, h), (w, 0))],
    # char W
    [((0, 0), (0, h)),
     ((0, h), (w/2, h/2 + h/4)),
     ((w, h), (w/2, h/2 + h/4)),
     ((w, 0), (w, h))],
    # char X
    [((0, 0), (w, h)),
     ((w, 0), (0, h))],
    # char Y
    [((0, 0), (w/2, h/4)),
     ((w, 0), (w/2, h/4)),
     ((w/2, h), (w/2, h/4)),
     ],
    # char Z
    [((0, 0), (w, 0)),
     ((w, 0), (0, h)),
     ((0, h), (w, h))],
]
