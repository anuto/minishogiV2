import unittest

# move to point to outer directory
from os import sys,path
FILE_PATH = path.abspath(__file__)
intended_path = FILE_PATH
for layer in range(4):
    intended_path = path.dirname(intended_path)
sys.path.append(intended_path)

from main.components.pieces.SilverGeneral import SilverGeneral
from main.components.pieces.PieceType import PieceType
from main.components.Game import Game

class SilverGeneralTest(unittest.TestCase):

    def test_initialization__correct_general_types(self):
        silver_general = SilverGeneral(1)
        self.assertFalse(silver_general.is_promoted)
        self.assertEquals(silver_general.type, PieceType.SILVER_GENERAL)

    def test_initialization__correct_placement__side_1(self):
        silver_general = SilverGeneral(1)
        self.assertEquals(silver_general.square, (0, 2))

    def test_initialization__correct_placement__side_2(self):
        silver_general = SilverGeneral(2)
        self.assertEquals(silver_general.square, (4, 2))

    def test_correct_valid_moves_on_placement__side_1(self):
        silver_general = SilverGeneral(1)
        game = self.setup_game()

        silver_general_moves = silver_general.get_valid_moves(game)
        expected_silver_general_moves = [
            (1, 1),
            (1, 2),
            (1, 3)
        ]

        self.assertItemsEqual(silver_general_moves, expected_silver_general_moves)

    def test_correct_valid_moves_on_placement__side_2(self):
        silver_general = SilverGeneral(2)
        game = self.setup_game()

        silver_general_moves = silver_general.get_valid_moves(game)
        expected_silver_general_moves = [
            (3, 1),
            (3, 2),
            (3, 3)
        ]

        self.assertItemsEqual(silver_general_moves, expected_silver_general_moves)

    def setup_game(self):
        game = Game()
        game.add_player("Fionna")
        game.add_player("Marshall")

        return game

if __name__ == '__main__':
    unittest.main()