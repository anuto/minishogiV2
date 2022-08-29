from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils

class Emperor(Piece):

	SIDE_1_STARTING_SQUARE = (0, 0)
	SIDE_2_STARTING_SQUARE = (4, 4)

	def get_base_type(self):
		return PieceType.EMPEROR

	def get_promote_type(self):
		raise Exception('emperor has no promote type, does not promote')

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