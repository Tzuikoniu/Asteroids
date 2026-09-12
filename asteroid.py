import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            a1_velocity= self.velocity.rotate(new_angle)
            a2_velocity= self.velocity.rotate(-new_angle)
            self.radius -= ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, self.radius)
            a2 = Asteroid(self.position.x, self.position.y, self.radius)
            a1.velocity = a1_velocity * 1.2
            a2.velocity = a2_velocity * 1.2
