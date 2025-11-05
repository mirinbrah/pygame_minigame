import pygame

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.x = float(self.screen_rect.centerx)
        self.y = self.screen_rect.bottom - 30
        self.color = 'gray'
        self.smoothing_factor = 0.1

    def update(self, mouse_x):
        # Robust way
        # self.x = mouse_x
        # Smooth way
        distance = mouse_x - self.x
        self.x += distance * self.smoothing_factor

        if self.x < 0:
            self.x = 0
        elif self.x > self.screen_rect.right:
            self.x = self.screen_rect.right

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 10)
        pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x, self.y - 20), 5)