import unittest

# move to point to outer directory
from os import sys,path
FILE_PATH = path.abspath(__file__)
intended_path = FILE_PATH
for layer in range(4):
    intended_path = path.dirname(intended_path)
sys.path.append(intended_path)

from main.components.pieces.Pawn import Pawn
from main.components.pieces.PieceType import PieceType
from main.components.Game import Game

class BishopTest(unittest.TestCase):

    def test_initialization__correct_general_types(self):
        pawn = Pawn(1)
        self.assertFalse(pawn.is_promoted)
        self.assertEquals(pawn.type, PieceType.PAWN)

    def test_initialization__correct_placement__side_1(self):
        pawn = Pawn(1)
        self.assertEquals(pawn.square, (1, 0))

    def test_initialization__correct_placement__side_2(self):
        pawn = Pawn(2)
        self.assertEquals(pawn.square, (3, 4))

    def test_correct_valid_moves_on_placement__side_1(self):
        pawn = Pawn(1)
        game = self.setup_game()

        pawn_moves = pawn.get_valid_moves(game)
        expected_pawn_moves = [
            (2, 0)
        ]

        self.assertItemsEqual(pawn_moves, expected_pawn_moves)

    def test_correct_valid_moves_on_placement__side_2(self):
        pawn = Pawn(2)
        game = self.setup_game()

        pawn_moves = pawn.get_valid_moves(game)
        expected_pawn_moves = [
            (2, 4)
        ]

        self.assertItemsEqual(pawn_moves, expected_pawn_moves)

    def setup_game(self):
        game = Game()
        game.add_player("Fionna")
        game.add_player("Marshall")

        return game

if __name__ == '__main__':
    unittest.main()