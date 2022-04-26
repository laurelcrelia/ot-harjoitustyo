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
        level = Level(self.level_2, self.size)
        renderer = Renderer(self.screen, level)
        menu = MenuView(self.screen)
        game_loop = GameLoop(level, self.screen, renderer,
                             self.size, self.clock, menu)
        game_loop.start()


if __name__ == "__main__":
    GAME = Game()
    GAME.main()
