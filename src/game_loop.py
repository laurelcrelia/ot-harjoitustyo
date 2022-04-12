import sys
import pygame


class GameLoop:
    def __init__(self, level, screen, renderer, cell_size, clock):
        self.level = level
        self.screen = screen
        self.renderer = renderer
        self.cell_size = cell_size
        self.clock = clock
        self.menu_screen_on = True
        self.level_completed_screen_on = True
        self.font1 = pygame.font.SysFont("Segoe UI", 50)
        self.font2 = pygame.font.SysFont("Segoe UI", 30)

    def start(self):
        while True:
            if self.movements() is False:
                break

            self.render()

            if self.level.is_completed() is True:
                self.draw_level_completed()

            self.clock.tick(60)

    def draw_menu(self):
        self.menu_initialization()

        while self.menu_screen_on:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.menu_screen_on = False
                if event.type == pygame.QUIT:
                    sys.exit()
        if not self.menu_screen_on:
            self.start()

    def draw_level_completed(self):
        self.level_completed_initialization()

        while self.level_completed_screen_on:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.level_completed_screen_on = False
                if event.type == pygame.QUIT:
                    sys.exit()
        if not self.menu_screen_on:
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

    def menu_initialization(self):
        self.screen.fill((169, 169, 169))
        game_title_text = self.font1.render("Labyrinth", False, (0, 0, 0))
        play_game_text = self.font2.render(
            "Start by pressing space", False, (205, 38, 38))
        self.screen.blit(game_title_text, (125, 130))
        self.screen.blit(play_game_text, (90, 200))
        pygame.display.update()

    def level_completed_initialization(self):
        self.screen.fill((151, 255, 255))
        level_passed_text = self.font2.render(
            "Gongratulations you passed this level!", False, (0, 0, 0))
        exit_text = self.font2.render(
            "Exit by pressing esc", False, (205, 38, 38))
        self.screen.blit(level_passed_text, (20, 130))
        self.screen.blit(exit_text, (90, 200))
        pygame.display.update()
