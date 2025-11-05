import pygame

from gun import Gun
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.play = True
        self.cannon = Gun(self.window)

    def run(self):
        while self.play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False

            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.cannon.update(mouse_x)

            self.window.fill(BLACK)
            self.cannon.draw()

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()