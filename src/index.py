import pygame
from pygame.locals import *
from level import Level


def main():

    level_1 = [[1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 0, 0, 1, 0, 0, 3, 1], 
        [1, 0, 0, 0, 0, 1, 1, 1], 
        [1, 1, 1, 1, 0, 0, 1, 1], 
        [1, 0, 0, 0, 1, 0, 0, 1], 
        [1, 0, 1, 0, 1, 1, 0, 1],
        [1, 2, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]

    size = 50

    level = Level(level_1,size)

    screen = pygame.display.set_mode((400,400))
    pygame.display.set_caption("Stickman")

    pygame.init()
    level.all_sprites.draw(screen)

    clock = pygame.time.Clock()
    clock.tick(60)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    level.move_stickman(x = -50)
                if event.key == K_RIGHT:
                    level.move_stickman(x = 50)
                if event.key == K_UP:
                    level.move_stickman(y = -50)
                if event.key == K_DOWN:
                    level.move_stickman(y = 50)
            elif event.type == QUIT:
                run = False

        pygame.display.update()
        level.all_sprites.draw(screen)


if __name__ == "__main__":
    main()
    


