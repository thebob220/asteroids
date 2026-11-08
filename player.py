from circleshape import CircleShape
from shot import Shot
from constants import *
import pygame

class Player(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:        # invert dt to go left
            self.rotate(dt * -1)    
        if keys[pygame.K_d]:        # right is easier
            self.rotate(dt)         
        if keys[pygame.K_w]:        # forward movement
            self.move(dt) 
        if keys[pygame.K_s]:        # reverse movement
            self.move(dt*-1)        
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt: float) -> None:
        vector = pygame.Vector2(0, 1)
        rvector = vector.rotate(self.rotation)
        mvector = rvector * PLAYER_SPEED * dt
        self.position += mvector

    def shoot(self) -> None:
        s = Shot(self.position.x, self.position.y)
        s.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED