import pygame

from gun import Gun
from bullet import Bullet
from settings import *
from target import Target


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.play = True

        self.cannon = Gun(self.window)
        self.bullets = pygame.sprite.Group()
        self.targets = pygame.sprite.Group()

        self.target_spawn_delay = 1000
        self.last_target_spawn = pygame.time.get_ticks()

    def spawn_targets(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_target_spawn > self.target_spawn_delay:
            self.last_target_spawn = current_time
            new_target = Target(self.window, WIDTH)
            self.targets.add(new_target)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    new_bullet = Bullet(self.window, self.cannon.x, self.cannon.y - 20, speed=10)
                    self.bullets.add(new_bullet)

    def update_game_state(self):
        mouse_x, _ = pygame.mouse.get_pos()
        self.cannon.update(mouse_x)

        self.bullets.update()
        self.targets.update()

        pygame.sprite.groupcollide(self.bullets, self.targets, True, True)

    def draw_elements(self):
        self.window.fill(BLACK)
        self.cannon.draw()

        self.bullets.draw(self.window)
        self.targets.draw(self.window)

        pygame.display.update()
        self.clock.tick(FPS)

    def run(self):
        while self.play:

            self.handle_events()

            self.update_game_state()

            self.draw_elements()
            self.spawn_targets()

        pygame.quit()

