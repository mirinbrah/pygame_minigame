import pygame
import random

class Target(pygame.sprite.Sprite):
    def __init__(self, screen, width_constraint, size=30, color='red'):
        super().__init__()
        self.screen = screen

        self.image = pygame.Surface((size, size))
        self.image.fill(pygame.Color(color))

        x = random.randint(0, width_constraint - size)
        y = random.randint(-150, -50)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.screen.get_height():
            self.kill()