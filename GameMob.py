# import pygame
import Position
import Vector


class GameMob(object):
    def __init__(self, width, height, maxspeed, maxacceleration, weight, friction, colour):
        self.width = width
        self.height = height
        self.MaxSpeed = maxspeed
        self.MaxAcceleration = maxacceleration
        self.Friction = friction
        self.Weight = weight
        self.Colour = colour
        self.vector = Vector.Vector(0, 0)
        self.position = Position.Position(0, 0)

    def Draw(self, screen):
        print("Not Drawing")

    def Animate(self):
        print("Not Animating")


