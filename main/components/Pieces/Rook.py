from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils

class Rook(Piece):
	def __init__(self, side):
		Piece.__init__(self, side)
		self.type = PieceType.ROOK

		self.square = PieceUtils.assign_based_on_side(side,
		 (0, 4), 
		 (4, 0)
	)

	def get_valid_moves(self, game):
		(y, x) = self.square
		potential_moves = []

		# check horizontal - left
		potential_moves += self.get_moves_in_horizontal_range(game, y, x - 1, -1, -1)

		# check horizontal - right
		potential_moves += self.get_moves_in_horizontal_range(game, y, x + 1, 5, 1)

		# check vertical - down
		potential_moves += self.get_moves_in_vertical_range(game, x, y - 1, 0, -1)

		# check vertical - up
		potential_moves += self.get_moves_in_vertical_range(game, x, y + 1, 5, 1)

		return potential_moves

	def get_moves_in_horizontal_range(self, game, y, start_range, end_range, step_size):
		potential_moves = []

		for x_i in range(start_range, end_range, step_size):
			potential_move = (y, x_i)
			if game.occupied_by_ally_piece(self.side, potential_move):
				return potential_moves 

			potential_moves.append(potential_move)

			if game.occupied_by_enemy_piece(self.side, potential_move):
				return potential_moves

		return potential_moves

	def get_moves_in_vertical_range(self, game, x, start_range, end_range, step_size):
		potential_moves = []

		for y_i in range(start_range, end_range, step_size):
			potential_move = (y_i, x)
			if game.occupied_by_ally_piece(self.side, potential_move):
				return potential_moves 

			potential_moves.append(potential_move)

			if game.occupied_by_enemy_piece(self.side, potential_move):
				return potential_moves

		return potential_moves