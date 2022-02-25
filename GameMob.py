# import pygame
import Point as pointLib
import Vector as vectorLib


class GameMob(object):
    def __init__(self, width, height, maxspeed, maxacceleration, weight, friction, colour):
        self.width = width
        self.height = height
        self.max_speed = maxspeed
        self.max_acceleration = maxacceleration
        self.friction = friction
        self.weight = weight
        self.colour = colour
        # self.vector = vectorLib.Vector(0.0, 0.0)
        self.position = pointLib.Point(0, 0)

    def draw(self, screen):
        print("Not Drawing")

    def animate(self):
        print("Not Animating")


