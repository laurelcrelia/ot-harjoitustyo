import pygame
from level import Level
from game_loop import GameLoop
from renderer import Renderer

def main():
    """Luo peliruudukon ja mahdollistaa ruudukossa liikkumisen"""

    level_1 = [[1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 0, 1, 0, 0, 3, 1],
               [1, 0, 0, 0, 0, 1, 1, 1],
               [1, 1, 1, 1, 0, 0, 1, 1],
               [1, 0, 0, 0, 1, 0, 0, 1],
               [1, 0, 1, 0, 1, 1, 0, 1],
               [1, 2, 1, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 1]]

    size = 50

    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Stickman")

    clock = pygame.time.Clock()
    clock.tick(60)

    level = Level(level_1, size)
    renderer = Renderer(screen, level)
    game_loop = GameLoop(level, renderer, size, clock)


    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
