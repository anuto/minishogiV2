import unittest

# move to point to outer directory
from os import sys,path
FILE_PATH = path.abspath(__file__)
intended_path = FILE_PATH
for layer in range(4):
    intended_path = path.dirname(intended_path)
sys.path.append(intended_path)

from main.components.pieces.Bishop import Bishop
from main.components.pieces.PieceType import PieceType
from main.components.Game import Game

class BishopTest(unittest.TestCase):

    def test_initialization__correct_general_types(self):
        bishop = Bishop(1)
        self.assertFalse(bishop.is_promoted)
        self.assertEquals(bishop.type, PieceType.BISHOP)

    def test_initialization__correct_placement__side_1(self):
        bishop = Bishop(1)
        self.assertEquals(bishop.square, (0, 3))

    def test_initialization__correct_placement__side_2(self):
        bishop = Bishop(2)
        self.assertEquals(bishop.square, (4, 1))

    def test_correct_valid_moves_on_placement__side_1(self):
        bishop = Bishop(1)
        game = self.setup_game()

        bishop_moves = bishop.get_valid_moves(game)
        expected_bishop_moves = [
            (1, 4),
            (1, 2),
            (2, 1),
            (3, 0)
        ]

        self.assertItemsEqual(bishop_moves, expected_bishop_moves)

    def test_correct_valid_moves_on_placement__side_2(self):
        bishop = Bishop(2)
        game = self.setup_game()

        bishop_moves = bishop.get_valid_moves(game)
        expected_bishop_moves = [
            (3, 0),
            (3, 2),
            (2, 3),
            (1, 4)
        ]

        self.assertItemsEqual(bishop_moves, expected_bishop_moves)

    def setup_game(self):
        game = Game()
        game.add_player("Fionna")
        game.add_player("Marshall")

        return game

if __name__ == '__main__':
    unittest.main()