from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils
from HelperFunctions import HelperFunctions as F

class Rook(Piece):
	
	SIDE_1_STARTING_SQUARE = (0, 4)
	SIDE_2_STARTING_SQUARE = (4, 0)

	def get_base_type(self):
		return PieceType.ROOK

	def get_promote_type(self):
		return PieceType.DRAGON_KING

	def get_valid_moves(self, game):
		(y, x) = self.square
		potential_moves = []

		potential_moves += self.get_north_moves(game, y, x)
		potential_moves += self.get_south_moves(game, y, x)
		potential_moves += self.get_east_moves(game, y, x)
		potential_moves += self.get_west_moves(game, y, x)

		if self.is_promoted:
			potential_moves += PieceUtils.get_move_diagonals(self, game, y, x)

		return potential_moves

	def get_north_moves(self, game, y, x):
		return PieceUtils.validate_moves(self, game, y, x,  F.increment, F.reflect)

	def get_south_moves(self, game, y, x):
		return PieceUtils.validate_moves(self, game, y, x,  F.decrement, F.reflect)

	def get_east_moves(self, game, y, x):
		return PieceUtils.validate_moves(self, game, y, x,  F.reflect, F.increment)

	def get_west_moves(self, game, y, x):
		return PieceUtils.validate_moves(self, game, y, x,  F.reflect, F.decrement)