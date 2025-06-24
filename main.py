import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for rock in asteroids:
            if rock.check_collisions(player):
                print("Game over!")
                return
        for rock in asteroids:
            for bullet in shots:
                if bullet.check_collisions(rock):
                    rock.split()
                    bullet.kill()
        for item in drawable:
            item.draw(screen)          
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()