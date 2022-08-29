import unittest

# move to point to outer directory
from os import sys,path
FILE_PATH = path.abspath(__file__)
intended_path = FILE_PATH
for layer in range(4):
    intended_path = path.dirname(intended_path)
sys.path.append(intended_path)

from main.components.pieces.Rook import Rook
from main.components.pieces.PieceType import PieceType
from main.components.Game import Game

class RookTest(unittest.TestCase):

    def test_initialization__correct_general_types(self):
        rook = Rook(1)
        self.assertFalse(rook.is_promoted)
        self.assertEquals(rook.type, PieceType.ROOK)

    def test_initialization__correct_placement__side_1(self):
        rook = Rook(1)
        self.assertEquals(rook.square, (0, 4))

    def test_initialization__correct_placement__side_2(self):
        rook = Rook(2)
        self.assertEquals(rook.square, (4, 0))

    def test_correct_valid_moves_on_placement__side_1(self):
        rook = Rook(1)
        game = self.setup_game()

        rook_moves = rook.get_valid_moves(game)
        expected_rook_moves = [
            (1, 4),
            (2, 4),
            (3, 4)
        ]

        self.assertItemsEqual(rook_moves, expected_rook_moves)

    def test_correct_valid_moves_on_placement__side_2(self):
        rook = Rook(2)
        game = self.setup_game()

        rook_moves = rook.get_valid_moves(game)
        expected_rook_moves = [
            (3, 0),
            (2, 0),
            (1, 0)
        ]

        self.assertItemsEqual(rook_moves, expected_rook_moves)

    def setup_game(self):
        game = Game()
        game.add_player("Fionna")
        game.add_player("Marshall")

        return game

if __name__ == '__main__':
    unittest.main()