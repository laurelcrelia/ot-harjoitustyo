import pygame


class MenuView:
    def __init__(self, screen):
        self.screen = screen

    def start_button(self):
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
                    return True
        if width-10 <= mouse[0] <= width+70 and height-5 <= mouse[1] <= height+35:
            pygame.draw.rect(self.screen, (190, 190, 190),
                             [width-10, height-5, 80, 40])
        else:
            pygame.draw.rect(self.screen, (100, 100, 100),
                             [width-10, height-5, 80, 40])

        self.screen.blit(play_text, (width, height))

    def exit_button(self):
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
                    pygame.quit()
        if width-10 <= mouse[0] <= width+70 and height-5 <= mouse[1] <= height+35:
            pygame.draw.rect(self.screen, (190, 190, 190),
                             [width-10, height-5, 80, 40])
        else:
            pygame.draw.rect(self.screen, (100, 100, 100),
                             [width-10, height-5, 80, 40])

        self.screen.blit(text, (width, height))

    def game_title(self):
        font1 = pygame.font.SysFont("Segoe UI", 50)
        game_title_text = font1.render("Labyrinth", False, (0, 0, 0))
        self.screen.fill((169, 169, 169))
        self.screen.blit(game_title_text, (100, 90))

    def initialize(self):
        while True:
            self.game_title()
            if self.start_button() is True:
                return False
            self.exit_button()
            pygame.display.update()

