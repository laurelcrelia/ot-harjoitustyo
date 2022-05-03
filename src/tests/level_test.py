import unittest

from level import Level

start_level = [[1, 1, 1, 1, 1, 1],
               [1, 3, 0, 0, 0, 1],
               [1, 1, 1, 1, 0, 1],
               [1, 0, 0, 0, 0, 1],
               [1, 2, 1, 4, 1, 1],
               [1, 1, 1, 1, 1, 1]]

size = 50


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.first_level = Level(start_level, size)

    def correct_coordinates(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_monster_coordinates_when_game_starts(self):
        monster = self.first_level.monster
        self.correct_coordinates(monster, size*3, size*4)

    def test_stickman_coordinates_when_game_starts(self):
        stickman = self.first_level.stickman
        self.correct_coordinates(stickman, size, size*4)

    def test_door_coordinates_when_game_starts(self):
        door = self.first_level.door
        self.correct_coordinates(door, size, size)

    def test_moving_is_possible(self):
        stickman = self.first_level.stickman
        self.correct_coordinates(stickman, size, size*4)

        self.first_level.move_stickman(y=-size)
        self.correct_coordinates(stickman, size, size*3)

        self.first_level.move_stickman(x=size)
        self.correct_coordinates(stickman, size*2, size*3)

    def test_moving_through_walls_is_impossible(self):
        stickman = self.first_level.stickman
        self.correct_coordinates(stickman, size, size*4)

        self.first_level.move_stickman(y=size)
        self.correct_coordinates(stickman, size, size*4)

        self.first_level.move_stickman(x=size)
        self.correct_coordinates(stickman, size, size*4)

    def test_moving_through_monster_is_impossible(self):
        stickman = self.first_level.stickman
        self.correct_coordinates(stickman, size, size*4)

        self.first_level.move_stickman(y=-size)
        self.correct_coordinates(stickman, size, size*3)

        self.first_level.move_stickman(x=size)
        self.correct_coordinates(stickman, size*2, size*3)

        self.first_level.move_stickman(x=size)
        self.correct_coordinates(stickman, size*3, size*3)

        self.first_level.move_stickman(y=+size)
        self.correct_coordinates(stickman, size*3, size*3)

    def test_moving_through_door_is_impossible(self):
        stickman = self.first_level.stickman
        self.correct_coordinates(stickman, size, size*4)

        self.first_level.move_stickman(y=-size)
        self.correct_coordinates(stickman, size, size*3)

        self.first_level.move_stickman(x=size*3)
        self.correct_coordinates(stickman, size*4, size*3)

        self.first_level.move_stickman(y=-size*2)
        self.correct_coordinates(stickman, size*4, size*1)

        self.first_level.move_stickman(x=-size*2)
        self.correct_coordinates(stickman, size*2, size*1)

        self.first_level.move_stickman(x=-size)
        self.correct_coordinates(stickman, size*2, size*1)

    # def correct_amount_of_hearts(self, hearts, amount):
    #     self.assertEqual(hearts, amount)

    # def test_stickman_dies(self):
    #     stickman = self.first_level.stickman
    #     amount_of_hearts = self.first_level.hearts

    #     self.correct_coordinates(stickman, size, size*4)

    #     self.first_level.move_stickman(y=-size)
    #     self.correct_amount_of_hearts(amount_of_hearts, 1)
    #     self.correct_coordinates(stickman, size, size*3)

    #     self.first_level.move_stickman(x=size)
    #     self.correct_amount_of_hearts(amount_of_hearts, 1)

    #     self.first_level.move_stickman(x=size)
    #     self.correct_amount_of_hearts(amount_of_hearts, 1)

    #     self.first_level.move_stickman(y=size)
    #     self.correct_amount_of_hearts(amount_of_hearts, 1)
    #     self.correct_coordinates(stickman, size*3, size*3)
