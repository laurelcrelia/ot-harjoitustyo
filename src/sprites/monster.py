import os
import pygame

dirname = os.path.dirname(__file__)


class Monster(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load(os.path.join(
            dirname, "..", "assets", "monster.png"))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.vel = 2

    def update_x(self):
        self.rect.x += self.vel

    def update_y(self):
        self.rect.y += self.vel
