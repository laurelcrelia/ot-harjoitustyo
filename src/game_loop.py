import pygame


class GameLoop:
    def __init__(self, level, renderer, cell_size, clock):
        self.level = level
        self.renderer = renderer
        self.cell_size = cell_size
        self.clock = clock

    def start(self):
        # self.menu_initialization()
        while True:
            if self.movements() is False:
                break

            self.render()

            self.clock.tick(60)

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
    #     self.screen.fill(0,0,0)
