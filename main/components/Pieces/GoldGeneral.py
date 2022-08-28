from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils

class GoldGeneral(Piece):
	def __init__(self, side):
		Piece.__init__(self, side)
		self.type = PieceType.GOLD_GENERAL
		self.square = PieceUtils.assign_based_on_side(side,
		 (0, 1), 
		 (4, 3)
		 )

	def get_valid_moves(self, game):
		(y, x) = self.square
		potential_moves = []

		# always check one square N
		potential_moves += self.validate_move(game, y + 1, x)		

		# always check one square E
		potential_moves += self.validate_move(game, y, x + 1)		

		# always check one square S
		potential_moves += self.validate_move(game, y - 1, x)		

		# always check one square W
		potential_moves += self.validate_move(game, y, x - 1)		

		# check diagonals - down if side 2, up if side 1
		if self.side == 1:
			potential_moves += self.validate_move(game, y + 1, x + 1)
			potential_moves += self.validate_move(game, y + 1, x - 1)

		else:
			potential_moves += self.validate_move(game, y - 1, x + 1)
			potential_moves += self.validate_move(game, y - 1, x - 1)

		return potential_moves

	def validate_move(self, game, y, x):
		if y < 0 or y > 4 or x < 0 or x > 4:
			return []

		potential_move = (y, x)
		if game.occupied_by_ally_piece(self.side, potential_move):
			return []
		else:
			return [potential_move]