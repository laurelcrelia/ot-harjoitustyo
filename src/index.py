import pygame
from pygame.locals import *
from level import Level


def main():

    level = Level()

    pygame.init()
    game_loop.start()

    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Stickman")

    clock = pygame.time.Clock()

    level.all_sprites.draw(screen)

    run = True

    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        level.all_sprites.draw(screen)
        clock.tick(60)


if __name__ == "__main__":
    main()
    


