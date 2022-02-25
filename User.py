import GameMob
import Car as carLib


class User(object):
    def __init__(self, name):
        self.name = str(name)
        # self.lives = int(Lives)
        self.car = carLib.Car(25, 50, 0, 0, 10, 10, (255, 0, 0))
