import pygame

class Bullet:
    def __init__(self, screen, x, y, speed, color='yellow', radius=2):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.radius = radius

    def update(self):
        self.y -= self.speed
        if self.y < 0:
            return False
        return True

    def draw(self):
        pygame.draw.circle(self.screen, pygame.Color(self.color),
                           (self.x, self.y),
                           self.radius)