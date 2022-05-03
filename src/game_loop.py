import sys
import pygame


class GameLoop:
    """Luokka kerää muuttujat vaadittaville parametreille."""

    def __init__(self, level, screen, renderer, cell_size, clock, menu):
        """Luokan konstruktori.

        Args:
            level:
                Level-luokan instanssi.
            screen:
                Pygame-olio joka hallitsee sovelluksen näkymää.
            renderer:
                Renderer-luokan instanssi.
            cell_size:
                Tasokartan ruudun pikselikoko.
            clock:
                Pygame kello.
            menu:
                Menu-luokan instanssi.
        """
        self.level = level
        self.screen = screen
        self.renderer = renderer
        self.cell_size = cell_size
        self.clock = clock
        self.menu = menu
        self.level_completed_screen_on = True
        self.game_over_screen_on = True

    def start(self):
        """Piirtää aloitusnäkymän ja käynnistää silmukan joka vaihtaa näkymää tietyn pelitilanteen mukaan."""
        self.menu.initialize()
        if self.menu.check == 1:
            while True:
                if self.movements() is False:
                    break

                self.render()

                if self.level.stickman_dies() is True:
                    self.draw_game_over()

                if self.level.is_completed() is True:
                    if self.draw_level_completed() is True:
                        return True

                self.clock.tick(60)
        elif self.menu.check == 2:
            sys.exit()

    def start_2(self):
        while True:
            if self.movements() is False:
                break

            self.render()

            if self.level.stickman_dies() is True:
                self.draw_game_over()

            if self.level.is_completed() is True:
                if self.draw_level_completed() is True:
                    return True

            self.clock.tick(60)

    def draw_level_completed(self):
        """Määrittää näkymän siitä kun taso on tullut läpäistyä ja piirtää sen kutsumalla metodia level_completed_initialization."""
        self.level_completed_initialization()

        while self.level_completed_screen_on:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return True
                if event.type == pygame.QUIT:
                    sys.exit()
        if not self.level_completed_screen_on:
            sys.exit()

    def draw_game_over(self):
        """Määrittää näkymän siitä kun peli on päättynyt häviöön ja piirtää sen kutsumalla metodia game_over_initialization."""
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
        """Määrittää pelihahmon liikuttamisen näppäimillä."""
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
        """Kutsuu luokan Renderer metodia "render" joka renderöi pelinäkymän."""
        self.renderer.render()

    def level_completed_initialization(self):
        """Piirtää läpäisynäkymän."""
        font1 = pygame.font.SysFont("Segoe UI", 22)
        font2 = pygame.font.SysFont("Segoe UI", 27)
        self.screen.fill((151, 255, 255))
        level_passed_text = font1.render(
            "Congratulations you passed this level!", False, (0, 0, 0))
        press_space_text = font2.render(
            "Press space for next level", False, (205, 38, 38))
        self.screen.blit(level_passed_text, (20, 120))
        self.screen.blit(press_space_text, (45, 170))
        pygame.display.update()

    def game_over_initialization(self):
        """Piirtää häviönäkymän."""
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
