import GameMob


class User(object):
    def __init__(self, Name, Lives):
        self.name = str(Name)
        self.lives = int(Lives)
        self.car = Car.Car(10, 10, 0, 0, 10, 10, (255, 255, 255))
