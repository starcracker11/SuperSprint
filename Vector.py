class Vector(float):
    def __init__(self, magnitude, angle):
        super().__init__()
        self.angle = angle
        self.magnitude = magnitude