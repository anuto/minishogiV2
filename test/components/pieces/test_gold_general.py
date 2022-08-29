import unittest

# move to point to outer directory
from os import sys,path
FILE_PATH = path.abspath(__file__)
intended_path = FILE_PATH
for layer in range(4):
    intended_path = path.dirname(intended_path)
sys.path.append(intended_path)

from main.components.pieces.GoldGeneral import GoldGeneral
from main.components.pieces.PieceType import PieceType
from main.components.Game import Game

class GoldGeneralTest(unittest.TestCase):

    def test_initialization__correct_general_types(self):
        gold_general = GoldGeneral(1)
        self.assertFalse(gold_general.is_promoted)
        self.assertEquals(gold_general.type, PieceType.GOLD_GENERAL)

    def test_initialization__correct_placement__side_1(self):
        gold_general = GoldGeneral(1)
        self.assertEquals(gold_general.square, (0, 1))

    def test_initialization__correct_placement__side_2(self):
        gold_general = GoldGeneral(2)
        self.assertEquals(gold_general.square, (4, 3))

    def test_correct_valid_moves_on_placement__side_1(self):
        gold_general = GoldGeneral(1)
        game = self.setup_game()

        gold_general_moves = gold_general.get_valid_moves(game)
        expected_gold_general_moves = [
            (1, 1),
            (1, 2)
        ]

        self.assertItemsEqual(gold_general_moves, expected_gold_general_moves)

    def test_correct_valid_moves_on_placement__side_2(self):
        gold_general = GoldGeneral(2)
        game = self.setup_game()

        gold_general_moves = gold_general.get_valid_moves(game)
        expected_gold_general_moves = [
            (3, 2),
            (3, 3)
        ]

        self.assertItemsEqual(gold_general_moves, expected_gold_general_moves)

    def setup_game(self):
        game = Game()
        game.add_player("Fionna")
        game.add_player("Marshall")

        return game

if __name__ == '__main__':
    unittest.main()