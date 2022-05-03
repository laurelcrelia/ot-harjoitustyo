import pygame
from level import Level
from game_loop import GameLoop
from renderer import Renderer
from menu import MenuView


class Game:
    def __init__(self):
        """Luokan konstruktori. Alustaa pelin käynnistystä varten tarvittavat parametrit.
        """
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
        self.list_of_maps = [self.level_1, self.level_2]
        self.index = 0
        self.current_level = self.list_of_maps[self.index]
        self.screen = pygame.display.set_mode((400, 450))
        pygame.display.set_caption("Labyrinth")
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

    def change_level(self):
        self.index += 1

    def main(self):
        """Luokka käynnistää pygamen ja luo Gameloop-luokan instanssin."""
        pygame.init()
        level_1 = Level(self.current_level, self.size)
        level_2 = Level(self.level_2, self.size)
        renderer_1 = Renderer(self.screen, level_1)
        renderer_2 = Renderer(self.screen, level_2)
        menu = MenuView(self.screen)
        game_loop_1 = GameLoop(level_1, self.screen, renderer_1,
                               self.size, self.clock, menu)
        game_loop_2 = GameLoop(level_2, self.screen, renderer_2,
                               self.size, self.clock, menu)
        game_loop_1.start()
        self.change_level()
        game_loop_2.start_2()


if __name__ == "__main__":
    GAME = Game()
    GAME.main()
