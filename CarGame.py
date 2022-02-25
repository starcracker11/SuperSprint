import pygame
import Track as trackLib
import GameMob
import User as userLib


class CarGame(object):
    def __init__(self):
        self.track = trackLib.Track()
        self.users = [userLib.User('Player 1'), userLib.User('Player 2')]

    def update(self):
        self.track.update()
