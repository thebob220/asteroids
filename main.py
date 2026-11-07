import constants
from logger import log_state
import pygame

def main():
    # printing starting guff
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    # init pygame
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

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

        pygame.display.flip()


if __name__ == "__main__":
    main()
