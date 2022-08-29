import unittest

# move to point to outer directory
from os import sys,path
FILE_PATH = path.abspath(__file__)
intended_path = FILE_PATH
for layer in range(4):
    intended_path = path.dirname(intended_path)
sys.path.append(intended_path)

from main.components.pieces.Emperor import Emperor
from main.components.pieces.PieceType import PieceType
from main.components.Game import Game

class BishopTest(unittest.TestCase):

    def test_initialization__correct_general_types(self):
        emperor = Emperor(1)
        self.assertFalse(emperor.is_promoted)
        self.assertEquals(emperor.type, PieceType.EMPEROR)

    def test_initialization__correct_placement__side_1(self):
        emperor = Emperor(1)
        self.assertEquals(emperor.square, (0, 0))

    def test_initialization__correct_placement__side_2(self):
        emperor = Emperor(2)
        self.assertEquals(emperor.square, (4, 4))

    def test_correct_valid_moves_on_placement__side_1(self):
        emperor = Emperor(1)
        game = self.setup_game()

        emperor_moves = emperor.get_valid_moves(game)
        expected_emperor_moves = [
            (1, 1)
        ]

        self.assertItemsEqual(emperor_moves, expected_emperor_moves)

    def test_correct_valid_moves_on_placement__side_2(self):
        emperor = Emperor(2)
        game = self.setup_game()

        emperor_moves = emperor.get_valid_moves(game)
        expected_emperor_moves = [
            (3, 3)
        ]

        self.assertItemsEqual(emperor_moves, expected_emperor_moves)

    def setup_game(self):
        game = Game()
        game.add_player("Fionna")
        game.add_player("Marshall")

        return game

if __name__ == '__main__':
    unittest.main()