import pygame
from constants import *
from circleshape import *

class Asteroid(CircleShape):


    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        #Asteroid.containers = (asteroids, updatable, drawable)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        #forward = pygame.Vector2
        self.position = self.position + (self.velocity * dt)

    def main():
        asteroids = pygame.sprite.Group
        
        