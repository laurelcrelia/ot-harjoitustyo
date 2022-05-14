import pygame
from level import Level
from game_loop import GameLoop
from renderer import Renderer
from menu import MenuView
from levels import LEVELS, SCREEN_X, SCREEN_Y


class Game:
    def __init__(self):
        """Luokan konstruktori. Alustaa pelin käynnistystä varten tarvittavat parametrit.
        """
        self.size = 50
        pygame.display.set_caption("Labyrinth")
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

    def main(self):
        """Luokka käynnistää pygamen ja luo Gameloop-luokan instanssin."""
        pygame.init()
        level_1 = Level(LEVELS[0], self.size)
        renderer_1 = Renderer(pygame.display.set_mode(
            (SCREEN_X[0], SCREEN_Y[0])), level_1)
        menu = MenuView(pygame.display.set_mode((SCREEN_X[0], SCREEN_Y[0])))
        screen = pygame.display.set_mode((SCREEN_X[0], SCREEN_Y[0]))
        game_loop_1 = GameLoop(level_1, screen, renderer_1,
                               self.size, self.clock, menu)
        game_loop_1.start()
        for i in range(1, 5):
            screen = pygame.display.set_mode((SCREEN_X[i], SCREEN_Y[i]))
            level_2 = Level(LEVELS[i], self.size)
            renderer_2 = Renderer(screen, level_2)
            game_loop_2 = GameLoop(level_2, screen, renderer_2,
                                   self.size, self.clock, menu)
            game_loop_2.start_2()


if __name__ == "__main__":
    GAME = Game()
    GAME.main()
