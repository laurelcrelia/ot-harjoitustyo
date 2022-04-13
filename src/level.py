import pygame
from sprites.stickman import Stickman
from sprites.wall import Wall
from sprites.floor import Floor
from sprites.door import Door


class Level:
    def __init__(self, level_map, cell_size):
        self.score = 0
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
                n_x = j * self.cell_size
                n_y = i * self.cell_size

                if cell == 0:
                    self.floors.add(Floor(n_x, n_y))
                elif cell == 1:
                    self.walls.add(Wall(n_x, n_y))
                elif cell == 2:
                    self.stickman = Stickman(n_x, n_y)
                    self.floors.add(Floor(n_x, n_y))
                elif cell == 3:
                    self.door = Door(n_x, n_y)
                    self.floors.add(Floor(n_x, n_y))
                # elif cell == 4:
                #     self.monster = Monster(n_x, n_y))
                #     self.floors.add(Floor(n_x, n_y))

        self.all_sprites.add(self.floors, self.walls, self.stickman, self.door)

    def movement_is_true(self, x=0, y=0):
        self.stickman.rect.move_ip(x, y)
        hitting_walls = pygame.sprite.spritecollide(
            self.stickman, self.walls, False)
        hitting_door = pygame.sprite.collide_rect(self.stickman, self.door)
        if hitting_door:
            self.stickman_finds_door()
        can_move = not hitting_walls and not hitting_door
        self.stickman.rect.move_ip(-x, -y)
        return can_move

    def move_stickman(self, x=0, y=0):
        if not self.movement_is_true(x, y):
            return
        self.stickman.rect.move_ip(x, y)

    def stickman_finds_door(self):
        self.score += 1

    def is_completed(self):
        if self.score > 0:
            return True
