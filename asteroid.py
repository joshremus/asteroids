import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # time to break em up and spawn them
            random_angle = random.uniform(20,50)
            vec1 = pygame.Vector2(self.position).rotate(random_angle)
            vec2 = pygame.Vector2(self.position).rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ass1 = Asteroid(self.position.x, self.position.y, new_radius)
            ass2 = Asteroid(self.position.x, self.position.y, new_radius)
            ass1.velocity = vec1 * 1.2
            ass2.velocity = vec2 * 1.2