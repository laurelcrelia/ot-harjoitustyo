import unittest

from level import Level

start_level = [[1,1,1,1,1,1],
            [1,3,0,0,0,1],
            [1,1,1,1,0,1],
            [1,0,0,0,0,1],
            [1,2,1,1,1,1]
            [1,1,1,1,1,1]]

size = 50


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.first_level =Level(start_level, size)

    def correct_coordinates(self, sprite, x, y):
        self.assertEqual(sprite.rect.x,x)
        self.assertEqual(sprite.rect.y,y)

    def moving_is_possible(self):
        stickman = self.first_level.stickman
        self.correct_coordinates(stickman, size, size*4)

        self.first_level.move_robot(y = -size)
        self.correct_coordinates(stickman, size, size*3)

        self.first_level.move_robot(x = size)
        self.correct_coordinates(stickman, size*2, size*3)

    def moving_through_walls_is_impossible(self):
        self.correct_coordinates(stickman, size, size*4)

        self.first_level.move_robot(y = size)
        self.correct_coordinates(stickman, size, size*4)

        self.first_level.move_robot(x = +size)
        self.correct_coordinates(stickman, size, size*4)

    

