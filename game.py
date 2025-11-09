import pygame

from gun import Gun
from bullet import Bullet
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.play = True

        self.cannon = Gun(self.window)
        self.bullets = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    new_bullet = Bullet(self.window, self.cannon.x, self.cannon.y - 20, speed=10)
                    self.bullets.append(new_bullet)

    def update_game_state(self):
        mouse_x, _ = pygame.mouse.get_pos()
        self.cannon.update(mouse_x)

        self.bullets = [bullet for bullet in self.bullets if bullet.update()]

        #variants
        #1-Longer
        # bullets_to_keep = []
        #
        # for bullet in self.bullets:
        #     if bullet.update():
        #         bullets_to_keep.append(bullet)
        #
        # self.bullets = bullets_to_keep
        # 2-Smarter

        #  len(self.bullets) - 1  -> индекс последнего элемента
        #  -1 -> до какого индекса идем (не включая)
        #  -1 -> шаг (назад)
        # for i in range(len(self.bullets) - 1, -1, -1):
             # Получаем пулю по ее индексу
        #     bullet = self.bullets[i]
        #
             # Если пуля улетела
        #     if not bullet.update():
        #        # удаляем ее по индексу
        #         self.bullets.pop(i)



    def draw_elements(self):
        self.window.fill(BLACK)
        self.cannon.draw()
        for bullet in self.bullets:
            bullet.draw()
        pygame.display.update()
        self.clock.tick(FPS)

    def run(self):
        while self.play:

            self.handle_events()

            self.update_game_state()

            self.draw_elements()



        pygame.quit()