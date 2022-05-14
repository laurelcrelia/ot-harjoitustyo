import pygame
from level import Level
from game_loop import GameLoop
from renderer import Renderer
from menu import MenuView
from levels import LEVELS


class Game:
    def __init__(self):
        """Luokan konstruktori. Alustaa pelin käynnistystä varten tarvittavat parametrit.
        """
        self.size = 50
        self.index = 0
        self.screen = pygame.display.set_mode((400, 450))
        pygame.display.set_caption("Labyrinth")
        self.clock = pygame.time.Clock()
        self.clock.tick(60)


    def change_level(self):
        self.index += 1

    def main(self):
        """Luokka käynnistää pygamen ja luo Gameloop-luokan instanssin."""
        pygame.init()
        level_1 = Level(LEVELS[self.index], self.size)
        renderer_1 = Renderer(self.screen, level_1)
        menu = MenuView(self.screen)
        game_loop_1 = GameLoop(level_1, self.screen, renderer_1,
                               self.size, self.clock, menu)
        game_loop_1.start()
        self.change_level()
        level_2 = Level(LEVELS[self.index], self.size)
        renderer_2 = Renderer(self.screen, level_2)
        game_loop_2 = GameLoop(level_2, self.screen, renderer_2,
                               self.size, self.clock, menu)
        game_loop_2.start_2()
        self.change_level()
        level_2 = Level(LEVELS[self.index], self.size)
        renderer_2 = Renderer(self.screen, level_2)
        game_loop_2 = GameLoop(level_2, self.screen, renderer_2,
                               self.size, self.clock, menu)
        game_loop_2.start_2()
        self.change_level()
        level_2 = Level(LEVELS[self.index], self.size)
        renderer_2 = Renderer(self.screen, level_2)
        game_loop_2 = GameLoop(level_2, self.screen, renderer_2,
                               self.size, self.clock, menu)
        game_loop_2.start_2()

if __name__ == "__main__":
    GAME = Game()
    GAME.main()
