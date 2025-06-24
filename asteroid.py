import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, (255, 255, 255), center, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()    
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            
            left_velocity = self.velocity.rotate(-random_angle) * 1.2
            right_velocity = self.velocity.rotate(random_angle) * 1.2
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            
            left_asteroid.velocity = left_velocity
            right_asteroid.velocity = right_velocity