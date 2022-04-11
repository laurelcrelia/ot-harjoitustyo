import pygame
from sprites.stickman import Stickman
from sprites.wall import Wall
from sprites.floor import Floor
from sprites.door import Door


class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.stickman = None
        self.door = None
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group()

        self._set_sprites(level_map)

    def _set_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for i in range(height):
            for j in range(width):
                cell = level_map[i][j]
                nx = j * self.cell_size
                ny = i * self.cell_size

                if cell == 0:
                    self.floors.add(Floor(nx, ny))
                elif cell == 1:
                    self.walls.add(Wall(nx, ny))
                elif cell == 2:
                    self.stickman = Stickman(nx, ny)
                    self.floors.add(Floor(nx, ny))
                elif cell == 3:
                    self.door = Door(nx, ny)
                    self.floors.add(Floor(nx, ny))

        self.all_sprites.add(self.floors, self.walls, self.stickman, self.door)

    def movement_is_true(self, x=0, y=0):
        self.stickman.rect.move_ip(x, y)
        hitting_walls = pygame.sprite.spritecollide(
            self.stickman, self.walls, False)
        can_move = not hitting_walls
        self.stickman.rect.move_ip(-x, -y)
        return can_move

    def move_stickman(self, x=0, y=0):
        if not self.movement_is_true(x, y):
            return
        self.stickman.rect.move_ip(x, y)
