import pygame
from constants import *
from circleshape import *

class Asteroid(CircleShape):


    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        #Asteroid.containers = (asteroids, updatable, drawable)

    def draw(self, x, y, radius, width):
        pygame.draw.circle("white", x, y, self.radius, 2)

    def update(self, dt):
        #forward = pygame.Vector2
        self.position = self.position + (self.velocity * dt)

    def main():
        asteroids = pygame.sprite.Group
        
        