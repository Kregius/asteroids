import pygame
from circleshape import CircleShape

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
        

