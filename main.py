import pygame
import sys
from shot import Shot
from logger import log_state, log_event
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # printing starting guff
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # init pygame malarkey
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    # groups for game objects
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # create game objects
    p = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    af = AsteroidField()

    # game loop
    while True:

        # logging
        log_state()

        # handle event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # make screen black
        screen.fill("black")

        # update, then draw objects
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)

        # check if the player collided with an asteroid
        for a in asteroids:
            if p.collides_with(a):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # update display
        pygame.display.flip()

        # clock stuff
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
