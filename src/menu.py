import pygame

class MenuView:
    def __init__(self, level, screen, renderer, cell_size, clock):
        self.level = level
        self.screen = screen
        self.renderer = renderer
        self.cell_size = cell_size
        self.clock = clock

    def start_button(self):
        width = 170
        height = 200
        font2 = pygame.font.SysFont("Segoe UI", 30)
        play_text = font2.render(
            "Play", True, (205, 38, 38))
        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if width-10 <= mouse[0] <= width+50 and height-5 <= mouse[1] <= height+25:
                        return False
            if width-10 <= mouse[0] <= width+50 and height-5 <= mouse[1] <= height+25:
                pygame.draw.rect(self.screen,(190,190,190),[width-10,height-5,60,30])
            else:
                pygame.draw.rect(self.screen,(100,100,100),[width-10,height-5,60,30])

            self.screen.blit(play_text, (width, height))
            pygame.display.update()

    def exit_button(self):
        width = 170
        height = 250
        font2 = pygame.font.SysFont("Segoe UI", 30)
        play_text = font2.render(
            "Exit", True, (205, 38, 38))
        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if width-10 <= mouse[0] <= width+50 and height-5 <= mouse[1] <= height+25:
                        pygame.quit()
            if width-10 <= mouse[0] <= width+50 and height-5 <= mouse[1] <= height+25:
                pygame.draw.rect(self.screen,(190,190,190),[width-10,height-5,60,30])
            else:
                pygame.draw.rect(self.screen,(100,100,100),[width-10,height-5,60,30])

            self.screen.blit(play_text, (width, height))
            pygame.display.update()

    def game_title(self):
        font1 = pygame.font.SysFont("Segoe UI", 50)
        game_title_text = font1.render("Labyrinth", False, (0, 0, 0))
        self.screen.fill((169, 169, 169))
        self.screen.blit(game_title_text, (100, 130))

    def initialize(self):
        self.game_title()
        self.exit_button()
        self.start_button()
        if self.start_button() is False:
            return False
        

                        

    # def draw(self):
    #     self.initialize()

    #     while self.menu_screen_on:
    #         for event in pygame.event.get():
    #             if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    #                 self.menu_screen_on = False
    #             if event.type == pygame.QUIT:
    #                 sys.exit()
    #     if not self.menu_screen_on:
    #         game = GameLoop(self.level, self.screen, self.renderer,
    #                          self.cell_size, self.clock)
    #         game.start()