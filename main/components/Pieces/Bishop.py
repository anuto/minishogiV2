from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils
from HelperFunctions import HelperFunctions as F

class Bishop(Piece):
	def __init__(self, side):
		Piece.__init__(self, side)
		self.type = PieceType.BISHOP
		self.square = PieceUtils.assign_based_on_side(side,
		 (0, 3), 
		 (4, 1)
		)
	
	def get_valid_moves(self, game):
		(y, x) = self.square
		potential_moves = []

		potential_moves += self.get_north_west_moves(game, y, x)		
		potential_moves += self.get_north_east_moves(game, y, x)		
		potential_moves += self.get_south_west_moves(game, y, x)		
		potential_moves += self.get_south_east_moves(game, y, x)

		if self.is_promoted:
			potential_moves += PieceUtils.get_move_nsew(self, game, y, x)

		return potential_moves

	def get_north_west_moves(self, game, y, x):
		return PieceUtils.validate_moves(self, game, y, x,  F.increment, F.decrement)

	def get_south_west_moves(self, game, y, x):
		return PieceUtils.validate_moves(self, game, y, x,  F.decrement, F.decrement)

	def get_north_east_moves(self, game, y, x):
		return PieceUtils.validate_moves(self, game, y, x,  F.increment, F.increment)

	def get_south_east_moves(self, game, y, x):
		return PieceUtils.validate_moves(self, game, y, x,  F.decrement, F.decrement)
