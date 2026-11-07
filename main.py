import constants
from logger import log_state
import pygame

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

        # update display
        pygame.display.flip()

        # clock stuff
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
