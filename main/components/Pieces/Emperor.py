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

		# always check one square N
		potential_moves += self.validate_move(game, y + 1, x)		

		# always check one square E
		potential_moves += self.validate_move(game, y, x + 1)		

		# always check one square S
		potential_moves += self.validate_move(game, y - 1, x)		

		# always check one square W
		potential_moves += self.validate_move(game, y, x - 1)

		# always check one square NW
		potential_moves += self.validate_move(game, y + 1, x - 1)		

		# always check one square NE
		potential_moves += self.validate_move(game, y + 1, x + 1)		

		# always check one square SE
		potential_moves += self.validate_move(game, y - 1, x + 1)		

		# always check one square SW
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