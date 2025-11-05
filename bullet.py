import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, speed, radius=5, color='yellow'):
        super().__init__()
        self.screen = screen

        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, pygame.Color(color), (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()