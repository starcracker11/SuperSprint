import GameMob


class Car(GameMob.GameMob):
    def __init__(self, width, height, maxspeed, maxacceleration, weight, friction, colour):
        super(Car, self).__init__(width, height, maxspeed, maxacceleration, weight, friction, colour)
        # while for ?? collision?