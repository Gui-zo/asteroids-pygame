import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, surface):
        pygame.draw.circle(surface, 'white', (int(self.position.x), int(self.position.y)), self.radius, 1)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            split_1 = Asteroid(self.position.x, self.position.y, self.radius / 2)
            split_1.velocity = (self.velocity * 1.2).rotate(random_angle)
            split_2 = Asteroid(self.position.x, self.position.y, self.radius / 2)
            split_2.velocity = (self.velocity * 1.2).rotate(-random_angle)