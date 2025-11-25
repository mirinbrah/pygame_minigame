import pygame
from gun import Gun
from bullet import Bullet
from settings import *
from target import Target
from ui_elements import Button


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

        self.score = 0
        self.font = pygame.font.Font(FONT_NAME, FONT_SIZE_NORMAL)
        self.font_large = pygame.font.Font(FONT_NAME, FONT_SIZE_LARGE)

        self.game_state = 'playing'

        btn_width, btn_height = 200, 50
        center_x = WIDTH // 2 - btn_width // 2

        self.btn_restart = Button(center_x, HEIGHT // 2, btn_width, btn_height,
                                  "Restart", self.font, BLACK, WHITE, (200, 200, 200))
        self.btn_quit = Button(center_x, HEIGHT // 2 + 70, btn_width, btn_height,
                               "Quit", self.font, BLACK, WHITE, (200, 200, 200))

    def reset_game(self):
        self.score = 0
        self.game_state = 'playing'
        self.targets.empty()
        self.bullets.empty()
        self.cannon.rect.centerx = self.cannon.screen_rect.centerx
        self.last_target_spawn = pygame.time.get_ticks()

    def spawn_targets(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_target_spawn > self.target_spawn_delay:
            self.last_target_spawn = current_time
            new_target = Target(self.window, WIDTH)
            self.targets.add(new_target)

    def check_collisions(self):
        hits = pygame.sprite.groupcollide(self.bullets, self.targets, True, True)
        if hits:
            for hit_targets in hits.values():
                self.score += len(hit_targets) * 10

        if pygame.sprite.spritecollide(self.cannon, self.targets, False):
            self.game_state = 'game_over'

    def update_game_state(self):
        mouse_x, _ = pygame.mouse.get_pos()
        self.cannon.update(mouse_x)
        self.bullets.update()
        self.targets.update()
        self.check_collisions()

    def draw_ui(self):
        score_text = f"Score: {self.score}"
        text_surface = self.font.render(score_text, True, WHITE)
        text_rect = text_surface.get_rect(topright=(WIDTH - 10, 10))
        self.window.blit(text_surface, text_rect)

    def run(self):
        while self.play:
            if self.game_state == 'playing':
                self.run_playing_state()
            elif self.game_state == 'game_over':
                self.run_gameover_state()
        pygame.quit()

    def run_playing_state(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    new_bullet = Bullet(self.window, self.cannon.rect.centerx, self.cannon.rect.top, speed=10)
                    self.bullets.add(new_bullet)

        self.spawn_targets()
        self.update_game_state()

        self.window.fill(BLACK)
        self.cannon.draw()
        self.bullets.draw(self.window)
        self.targets.draw(self.window)
        self.draw_ui()

        pygame.display.update()
        self.clock.tick(FPS)

    def run_gameover_state(self):
        self.window.fill(BLACK)

        game_over_text = self.font_large.render("GAME OVER", True, WHITE)
        score_text = self.font.render(f"Your Score: {self.score}", True, WHITE)

        self.window.blit(game_over_text, game_over_text.get_rect(centerx=WIDTH // 2, centery=HEIGHT // 3))
        self.window.blit(score_text, score_text.get_rect(centerx=WIDTH // 2, centery=HEIGHT // 3 + 80))

        mouse_pos = pygame.mouse.get_pos()
        self.btn_restart.check_hover(mouse_pos)
        self.btn_quit.check_hover(mouse_pos)

        self.btn_restart.draw(self.window)
        self.btn_quit.draw(self.window)

        pygame.display.update()
        self.clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.play = False

            if self.btn_restart.is_clicked(mouse_pos, event):
                self.reset_game()
            if self.btn_quit.is_clicked(mouse_pos, event):
                self.play = False