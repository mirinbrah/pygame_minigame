import pygame
import random
from settings import *


class Target(pygame.sprite.Sprite):
    def __init__(self, screen, width_constraint, speed_multiplier=1.0, obj_type='enemy'):
        super().__init__()
        self.screen = screen
        self.obj_type = obj_type  # 'enemy' или 'heal'
        size = 30

        self.image = pygame.Surface((size, size), pygame.SRCALPHA)

        if self.obj_type == 'heal':
            pygame.draw.circle(self.image, GREEN, (size // 2, size // 2), size // 2)
        else:
            self.image.fill(pygame.Color('red'))

        x = random.randint(0, width_constraint - size)
        y = random.randint(-150, -50)
        self.rect = self.image.get_rect(topleft=(x, y))

        base_speed = random.randint(2, 5)
        self.speed = base_speed * speed_multiplier

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.screen.get_height():
            self.kill()