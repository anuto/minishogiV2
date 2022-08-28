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
		if self.side == 1:
			potential_move = [(self.square[0] + 1, self.square[1])]
		else:
			potential_move = [(self.square[0] - 1, self.square[1])]

		if game.occupied_by_enemy_piece(self.side, potential_move):
			return []

		return [potential_move]
