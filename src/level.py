import pygame
from sprites.stickman import Stickman
from sprites.platform import Platform
from sprites.door import Door

class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.stickman = None
        self.door = None
        self.platforms = pygame.sprite.Group()

        self.all_sprites = pygame.sprite.Group()

        self._set_sprites(level_map)

    def _set_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for i in range(height):
            for j in range(width):
                cell = level_map[i][j]
                x = j * self.cell_size
                y = i * self.cell_size

                if cell == 0:
                    pass
                elif cell == 1:
                    self.platforms.add(Platform(x,y))
                elif cell == 2:
                    self.stickman.add(Stickman(x,y))
                elif cell == 3:
                    self.door.add(Door(x,y))

        self.all_sprites.add(self.stickman, self.door, self,platforms)

    #robon liike seinien välissä
        if self.oikea:
            if self.x+self.stickman.get_width() >= 640:
                self.x = self.x
            else:
                self.x += 2
        if self.vasen:
            if self.x+self.stickman.get_width() <= 50:
                self.x = self.x
            else:
                self.x -= 2


    def movement_is_true(self, x=0, y=0):
        self.stickman.rect.move_ip(x,y)
        hitting_walls = pygame.sprite.spritecollide(self.stickman, self.platforms, False)
        can_move = not hitting_walls
        self.stickman.rect.move_ip(-x,-y)
        return can_move

    def move_stickman(self, x=0, y=0):
        if not self.movement_is_true(x,y):
            return 
        self.stickman.rect.move_ip(x,y)



