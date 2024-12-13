import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):


    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

        shots = pygame.sprite.Group
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)

