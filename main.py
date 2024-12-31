import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    pointscore = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf',32)
    text = font.render(f'Score: {pointscore}',True,"white","black")
    textRect = text.get_rect()
    textRect.center =(SCREEN_WIDTH // 10, SCREEN_HEIGHT // 20)


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collidesWith(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collidesWith(shot):
                    shot.kill()
                    asteroid.split()
                    pointscore += 1

        screen.fill("black")
        text = font.render(f'Score: {pointscore}',True,"white","black")
        screen.blit(text, textRect)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()