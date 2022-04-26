import sys
import pygame


class GameLoop:
    def __init__(self, level, screen, renderer, cell_size, clock, menu):
        self.level = level
        self.screen = screen
        self.renderer = renderer
        self.cell_size = cell_size
        self.clock = clock
        self.menu = menu
        self.level_completed_screen_on = True
        self.game_over_screen_on = True

    def start(self):
        if self.menu.initialize() is False:
            while True:
                if self.movements() is False:
                    break

                self.render()

                if self.level.stickman_dies() is True:
                    self.draw_game_over()

                if self.level.is_completed() is True:
                    self.draw_level_completed()

                self.clock.tick(60)

    def draw_level_completed(self):
        self.level_completed_initialization()

        while self.level_completed_screen_on:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.level_completed_screen_on = False
                if event.type == pygame.QUIT:
                    sys.exit()
        if not self.level_completed_screen_on:
            sys.exit()

    def draw_game_over(self):
        self.game_over_initialization()

        while self.game_over_screen_on:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.game_over_screen_on = False
                if event.type == pygame.QUIT:
                    sys.exit()
        if not self.game_over_screen_on:
            sys.exit()

    def movements(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.level.move_stickman(x=-50)
                if event.key == pygame.K_RIGHT:
                    self.level.move_stickman(x=50)
                if event.key == pygame.K_UP:
                    self.level.move_stickman(y=-50)
                if event.key == pygame.K_DOWN:
                    self.level.move_stickman(y=50)
            elif event.type == pygame.QUIT:
                return False

    def render(self):
        self.renderer.render()

    # def menu_initialization(self):
    #     font1 = pygame.font.SysFont("Segoe UI", 50)
    #     font2 = pygame.font.SysFont("Segoe UI", 30)
    #     self.screen.fill((169, 169, 169))
    #     game_title_text = font1.render("Labyrinth", False, (0, 0, 0))
    #     play_game_text = font2.render(
    #         "Start by pressing space", False, (205, 38, 38))
    #     self.screen.blit(game_title_text, (100, 130))
    #     self.screen.blit(play_game_text, (60, 200))
    #     pygame.display.update()

    def level_completed_initialization(self):
        font1 = pygame.font.SysFont("Segoe UI", 22)
        font2 = pygame.font.SysFont("Segoe UI", 27)
        self.screen.fill((151, 255, 255))
        level_passed_text = font1.render(
            "Gongratulations you passed this level!", False, (0, 0, 0))
        exit_text = font2.render(
            "Exit by pressing esc", False, (205, 38, 38))
        self.screen.blit(level_passed_text, (15, 130))
        self.screen.blit(exit_text, (70, 200))
        pygame.display.update()

    def game_over_initialization(self):
        font1 = pygame.font.SysFont("Segoe UI", 35)
        font2 = pygame.font.SysFont("Segoe UI", 27)
        self.screen.fill((151, 255, 255))
        level_game_over_text = font1.render(
            "Game Over :(", False, (0, 0, 0))
        exit_text = font2.render(
            "Exit by pressing esc", False, (205, 38, 38))
        self.screen.blit(level_game_over_text, (70, 130))
        self.screen.blit(exit_text, (70, 200))
        pygame.display.update()
