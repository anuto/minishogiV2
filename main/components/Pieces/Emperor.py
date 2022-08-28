from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils

class Emperor(Piece):
	def __init__(self, side):
		Piece.__init__(self, side)
		self.type = PieceType.EMPEROR
		self.square = PieceUtils.assign_based_on_side(side,
		 (0, 0), 
		 (4, 4)
		 )

	def get_valid_moves(self, game):
		(y, x) = self.square
		potential_moves = []

		potential_moves += PieceUtils.get_move_nsew(self, game, y, x)	
		potential_moves += PieceUtils.get_move_diagonals(self, game, y, x)

		return potential_moves

	def can_promote(self):
		return False

	def promote(self):
		raise Exception("why are u trying to promote the emperor D:")