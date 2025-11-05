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
        self.bullets = []
        self.targets = []

        self.target_spawn_delay = 1000
        self.last_target_spawn = pygame.time.get_ticks()

    def spawn_targets(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_target_spawn > self.target_spawn_delay:
            self.last_target_spawn = current_time
            new_target = Target(self.window, WIDTH)
            self.targets.append(new_target)

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
        self.targets = [target for target in self.targets if target.update()]
        self.check_collisions()

    def draw_elements(self):
        self.window.fill(BLACK)
        self.cannon.draw()
        for bullet in self.bullets:
            bullet.draw()
        for target in self.targets:
            target.draw()
        pygame.display.update()
        self.clock.tick(FPS)

    def run(self):
        while self.play:

            self.handle_events()

            self.update_game_state()

            self.draw_elements()
            self.spawn_targets()

        pygame.quit()

    def check_collisions(self):
        for bullet in self.bullets[:]:
            for target in self.targets[:]:
                if bullet.rect.colliderect(target.rect):
                    self.bullets.remove(bullet)
                    self.targets.remove(target)
                    break