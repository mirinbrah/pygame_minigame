import pygame

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color = 'gray'
        self.smoothing_factor = 0.1

        self.image = pygame.Surface((20, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (10, 20), 10)
        pygame.draw.line(self.image, self.color, (10, 20), (10, 0), 5)

        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

    def update(self, mouse_x):
        # Robust way
        # self.x = mouse_x
        # Smooth way
        target_x = mouse_x
        distance = target_x - self.rect.centerx
        self.rect.centerx += distance * self.smoothing_factor

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right

    def draw(self):
        self.screen.blit(self.image, self.rect)