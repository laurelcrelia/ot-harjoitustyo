import unittest
import pygame

from menu import MenuView

screen = pygame.display.set_mode((400, 400))


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.first_level = MenuView(screen)
