from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils

class Pawn(Piece):
	def __init__(self, side):
		Piece.__init__(self, side)
		self.type = PieceType.PAWN
		self.square = PieceUtils.assign_based_on_side(side,
		 (1, 0), 
		 (3, 4)
		 )

	def get_valid_moves(self, game):
		(y, x) = self.square

		if self.side == 1:
			return self.validate_move(game, y + 1, x)

		else:
			return self.validate_move(game, y - 1, x)

	def validate_move(self, game, y, x):
		if y < 0 or y > 4 or x < 0 or x > 4:
			return []

		potential_move = (y, x)
		if game.occupied_by_ally_piece(self.side, potential_move):
			return []
		else:
			return [potential_move]