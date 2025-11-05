import pygame
import random


class Target:
    def __init__(self, screen, width_constraint):
        self.screen = screen
        self.size = 30

        x = random.randint(0, width_constraint - self.size)
        y = random.randint(-150, -50)

        self.rect = pygame.Rect(x, y, self.size, self.size)

        self.speed = random.randint(1, 3)
        self.color = 'red'

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > self.screen.get_height():
            return False
        return True

    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color(self.color), self.rect)