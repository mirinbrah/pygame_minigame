import pygame

class Bullet:
    def __init__(self, screen, x, y, speed, color='yellow', radius=2):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.radius = radius
        #for collision check with targets
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
        if self.rect.bottom < 0:
            return False
        return True

    def draw(self):
        pygame.draw.circle(self.screen, pygame.Color(self.color),
                           (self.x, self.y),
                           self.radius)