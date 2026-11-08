from circleshape import CircleShape
from constants import *
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        # remove original sprite
        self.kill()

        # check if asteroid is too small
        if self.radius == ASTEROID_MIN_RADIUS:
            return

        # log asteroid splitting
        log_event("asteroid_split")

        # create angled velocities for asteroid split
        split_angle = random.uniform(20, 50)
        a1v = self.velocity.rotate(split_angle) * 1.2
        a2v = self.velocity.rotate(split_angle * -1) * 1.2

        new_rad = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_rad)
        a1.velocity = a1v
        a2 = Asteroid(self.position.x, self.position.y, new_rad)
        a2.velocity = a2v
