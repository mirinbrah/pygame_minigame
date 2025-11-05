import pygame

from settings import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.play = True

    def run(self):
        while self.play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()


