import constants
from logger import log_state
import pygame
from player import Player

def main():
    # printing starting guff
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    # init pygame malarkey
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    # group up objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # create game objects
    p = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

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

        # update display
        pygame.display.flip()

        # clock stuff
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
