from Player import Player 

from pieces.Emperor import Emperor
from pieces.GoldGeneral import GoldGeneral
from pieces.SilverGeneral import SilverGeneral
from pieces.Bishop import Bishop
from pieces.Rook import Rook
from pieces.Pawn import Pawn

from pieces.PieceType import PieceType

from os import sys,path
PARENT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(PARENT_DIR)

from Player import Player

class Side(object):

	# param name should be a string name of the player
	def __init__(self, name, side_number):
		self.player = Player(name)
		self.captured = []
		self.side = side_number
		self.pieces = self.create_starting_pieces(side_number)

	def create_starting_pieces(self, side):
		return [
			Pawn(side),
			Bishop(side),
			Rook(side),
			SilverGeneral(side),
			GoldGeneral(side),
			Emperor(side)
		]

	def place_piece(self, piece, placement_square):
		self.captured.remove(piece)
		self.pieces.append(piece)
		piece.move_piece(placement_square)

	def add_captured_piece(self, piece):
		self.captured.append(piece)

	def piece_captured(self, piece):
		self.pieces.remove(piece)
		piece.captured()

	# returns if the player has lost
	def lost(self):
		for piece in self.pieces:
			if piece.type == PieceType.EMPEROR:
				return False
		return True