from Player import Player 

from Pieces.Emperor import Emperor
from Pieces.GoldGeneral import GoldGeneral
from Pieces.SilverGeneral import SilverGeneral
from Pieces.Bishop import Bishop
from Pieces.Rook import Rook
from Pieces.Pawn import Pawn

from Pieces.PieceType import PieceType

from os import sys,path
PARENT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(PARENT_DIR)

from Player import Player

class Side(object):

	# param name should be a string name of the player
	def __init__(self, name, side):
		self.player = Player(name)
		self.pieces = self.create_starting_pieces(side)
		self.captured = []
		self.side = side

	def create_starting_pieces(self, side):
		return [
			Pawn(side),
			Bishop(side),
			Rook(side),
			SilverGeneral(side),
			GoldGeneral(side),
			Emperor(side)
		]

	# returns if the player has lost
	def lost(self):
		for piece in self.pieces:
			if piece.type == PieceType.EMPEROR:
				return False
		return True