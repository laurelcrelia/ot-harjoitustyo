import pygame
from sprites.stickman import Stickman
from sprites.wall import Wall
from sprites.floor import Floor
from sprites.door import Door
from sprites.monster import Monster
from levels import LEVELS


class Level:  # pylint: disable=too-many-instance-attributes # all these instance attributes are necessary
    def __init__(self, level_map, cell_size):
        self.score = 0
        self.hearts = 1
        self.cell_size = cell_size
        self.level_map = level_map
        self.stickman = None
        self.door = None
        self.x_monsters = pygame.sprite.Group()
        self.y_monsters = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._set_sprites(level_map)

    def _set_sprites(self, level_map):  # pylint: disable=too-many-statements
        # these statements are required otherwise there would be monster in the first level
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
                elif cell == 4:
                    self.x_monsters.add(Monster(n_x, n_y))
                    self.floors.add(Floor(n_x, n_y))
                elif cell == 5:
                    self.y_monsters.add(Monster(n_x, n_y))
                    self.floors.add(Floor(n_x, n_y))

        if self.level_map == LEVELS[0]:
            self.all_sprites.add(self.floors, self.walls,
                                 self.stickman, self.door)
        else:
            self.all_sprites.add(self.floors, self.walls,
                                 self.x_monsters, self.y_monsters, self.stickman, self.door)

    def movement_is_true(self, x=0, y=0):
        self.stickman.rect.move_ip(x, y)
        hitting_walls = pygame.sprite.spritecollide(
            self.stickman, self.walls, False)
        hitting_door = pygame.sprite.collide_rect(self.stickman, self.door)
        if hitting_door:
            self.score += 1
        can_move = not hitting_walls and not hitting_door
        if self.level_map != LEVELS[0]:
            hitting_x_monsters = pygame.sprite.spritecollide(
                self.stickman, self.x_monsters, False)
            hitting_y_monsters = pygame.sprite.spritecollide(
                self.stickman, self.y_monsters, False)
            hitting_monsters = hitting_x_monsters or hitting_y_monsters
            if hitting_monsters:
                self.hearts -= 1
            can_move = not hitting_walls and not hitting_door and not hitting_monsters
        self.stickman.rect.move_ip(-x, -y)
        return can_move

    def move_stickman(self, x=0, y=0):
        if not self.movement_is_true(x, y):
            return
        self.stickman.rect.move_ip(x, y)

    def move_x_monsters(self):
        for monster in self.x_monsters:
            monster.update_x()
            hitting_walls = pygame.sprite.spritecollide(
                monster, self.walls, False)
            hitting_door = pygame.sprite.collide_rect(monster, self.door)
            if hitting_walls or hitting_door:
                monster.vel *= -1

    def move_y_monsters(self):
        for monster in self.y_monsters:
            monster.update_y()
            hitting_walls = pygame.sprite.spritecollide(
                monster, self.walls, False)
            hitting_door = pygame.sprite.collide_rect(monster, self.door)
            if hitting_walls or hitting_door:
                monster.vel *= -1
