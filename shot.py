import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):


    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        #Asteroid.containers = (asteroids, updatable, drawable)

    def draw(position, screen):
        pygame.draw.circle(screen, "white", position, SHOT_RADIUS, 2)

    def update(self, dt):
        #forward = pygame.Vector2
        self.position = self.position + (self.velocity * dt)

    def main():
        shots = pygame.sprite.Group
        
        



'''
import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):


    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

        shots = pygame.sprite.Group
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)

'''