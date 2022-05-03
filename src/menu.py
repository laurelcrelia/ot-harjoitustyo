import pygame


class MenuView:
    """Pelin alkoitusnäkymästä vastaava luokka."""

    def __init__(self, screen):
        """Luokan konstruktori. Luo pelin aloitusnäkymän.

        Args:
            screen:
                Elementti joka alustaa ikkunan.
        """
        self.screen = screen
        self.check = 0

    def play_button(self):
        """Määrittää "play"-painikkeen toiminnan."""
        width = 170
        height = 180
        font2 = pygame.font.SysFont("Segoe UI", 30)
        play_text = font2.render(
            "Play", True, (205, 38, 38))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width-10 <= mouse[0] <= width+70 and height-5 <= mouse[1] <= height+35:
                    self.check += 1
        if width-10 <= mouse[0] <= width+70 and height-5 <= mouse[1] <= height+35:
            pygame.draw.rect(self.screen, (190, 190, 190),
                             [width-10, height-5, 80, 40])
        else:
            pygame.draw.rect(self.screen, (100, 100, 100),
                             [width-10, height-5, 80, 40])

        self.screen.blit(play_text, (width, height))

    def exit_button(self):
        """Määrittää "exit"-painikkeen toiminnan."""
        width = 170
        height = 240
        font2 = pygame.font.SysFont("Segoe UI", 30)
        text = font2.render(
            "Exit", True, (205, 38, 38))
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width-10 <= mouse[0] <= width+70 and height-5 <= mouse[1] <= height+35:
                    self.check += 2
        if width-10 <= mouse[0] <= width+70 and height-5 <= mouse[1] <= height+35:
            pygame.draw.rect(self.screen, (190, 190, 190),
                             [width-10, height-5, 80, 40])
        else:
            pygame.draw.rect(self.screen, (100, 100, 100),
                             [width-10, height-5, 80, 40])

        self.screen.blit(text, (width, height))

    def game_title(self):
        """Määrittää peli-ikkunan otsikon."""
        font1 = pygame.font.SysFont("Segoe UI", 50)
        game_title_text = font1.render("Labyrinth", False, (0, 0, 0))
        self.screen.fill((169, 169, 169))
        self.screen.blit(game_title_text, (100, 90))

    def initialize_game_title(self):
        """Asettaa peli-ikkunan otsikon."""
        self.game_title()

    def initialize_play_button(self):
        """Asettaa "play"-painikkeen tilan."""
        self.play_button()

    def initialize_exit_button(self):
        """Asettaa "exit"-painikkeen tilan."""
        self.exit_button()

    def initialize(self):
        """Määrittää aloitusnäkymän ja tarkistaa painikkeiden tilan."""
        while self.check == 0:
            self.initialize_game_title()
            self.initialize_play_button()
            self.initialize_exit_button()
            pygame.display.update()
