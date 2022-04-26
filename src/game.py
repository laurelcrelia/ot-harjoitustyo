import pygame
from level import Level
from game_loop import GameLoop
from renderer import Renderer
from menu import MenuView


class Game:
    def __init__(self):
        self.size = 50
        self.level_1 = [[1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 1, 0, 0, 3, 1],
                        [1, 0, 0, 0, 0, 1, 1, 1],
                        [1, 1, 1, 1, 0, 0, 1, 1],
                        [1, 0, 0, 0, 1, 0, 0, 1],
                        [1, 0, 1, 0, 1, 1, 0, 1],
                        [1, 2, 1, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1]]

        self.level_2 = [[1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 1, 0, 0, 3, 1],
                        [1, 4, 0, 0, 0, 1, 1, 1],
                        [1, 1, 1, 1, 0, 0, 1, 1],
                        [1, 0, 0, 0, 1, 0, 0, 1],
                        [1, 0, 1, 0, 1, 1, 0, 1],
                        [1, 2, 1, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1]]

        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Labyrinth")
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

    def main(self):
        """Luo peliruudukon ja mahdollistaa ruudukossa liikkumisen"""
        pygame.init()
        level_1 = Level(self.level_1, self.size)
        level_2 = Level(self.level_2, self.size)
        renderer_1 = Renderer(self.screen, level_1)
        renderer_2 = Renderer(self.screen, level_2)
        menu = MenuView(self.screen)
        game_loop_1 = GameLoop(level_1, self.screen, renderer_1,
                               self.size, self.clock, menu)
        game_loop_2 = GameLoop(level_2, self.screen, renderer_2,
                               self.size, self.clock, menu)
        if game_loop_1.start() is True:
            game_loop_2.start_2()


if __name__ == "__main__":
    GAME = Game()
    GAME.main()
