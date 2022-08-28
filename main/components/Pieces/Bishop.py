from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils

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

		# check NW
		y_i = y + 1
		x_i = x - 1

		while(y_i < 5 and x_i > -1):
			potential_move = (y_i, x_i)
			if game.occupied_by_ally_piece(self.side, potential_move):
				break
			potential_moves.append(potential_move)
			if game.occupied_by_enemy_piece(self.side, potential_move):
				break

			y_i += 1
			x_i -= 1


		# check NE
		y_i = y + 1
		x_i = x + 1

		while(y_i < 5 and x_i < 5):
			potential_move = (y_i, x_i)
			if game.occupied_by_ally_piece(self.side, potential_move):
				break
			potential_moves.append(potential_move)
			if game.occupied_by_enemy_piece(self.side, potential_move):
				break

			y_i += 1
			x_i += 1

		# check SW
		y_i = y - 1
		x_i = x - 1

		while(y_i > -1 and x_i > -1):
			potential_move = (y_i, x_i)
			if game.occupied_by_ally_piece(self.side, potential_move):
				break
			potential_moves.append(potential_move)
			if game.occupied_by_enemy_piece(self.side, potential_move):
				break

			y_i -= 1
			x_i -= 1

		# check SE
		y_i = y - 1
		x_i = x + 1

		while(y_i > -1 and x_i < 5):
			potential_move = (y_i, x_i)
			if game.occupied_by_ally_piece(self.side, potential_move):
				break
			potential_moves.append(potential_move)
			if game.occupied_by_enemy_piece(self.side, potential_move):
				break

			y_i -= 1
			x_i += 1
			
		return potential_moves
