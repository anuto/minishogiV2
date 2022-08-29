class PieceUtils:

	@staticmethod
	def validate_square(square):
		(y, x) = square
		return y >= 0 and y <= 4 and x >= 0 and x <= 4

	# returns the move as a single item [list] if it is valid
	@staticmethod
	def validate_move(piece, game, y, x):
		potential_move = (y, x)
		if not PieceUtils.validate_square(potential_move):
			return []

		if game.square_occupied_by_ally_piece(piece.side, potential_move):
			return []
		else:
			return [potential_move]

	@staticmethod
	def validate_moves(piece, game, y, x, y_change, x_change):
		potential_moves = []

		y_i = y_change(y)
		x_i = x_change(x)

		potential_move = (y_i, x_i)
		while(PieceUtils.validate_square(potential_move)):
			if game.square_occupied_by_ally_piece(piece.side, potential_move):
				return potential_moves

			potential_moves.append(potential_move)
			
			if game.square_occupied_by_enemy_piece(piece.side, potential_move):
				return potential_moves

			y_i = y_change(y_i)
			x_i = x_change(x_i)

			potential_move = (y_i, x_i)

		return potential_moves

			
### Movement Utils ###
	### --- Grouping Single Square Functions ###
	@staticmethod
	def get_move_nsew(piece, game, y, x):
		moves = []
		moves += PieceUtils.get_move_north(piece, game, y, x)
		moves += PieceUtils.get_move_south(piece, game, y, x)
		moves += PieceUtils.get_move_east(piece, game, y, x)
		moves += PieceUtils.get_move_west(piece, game, y, x)
		return moves

	@staticmethod
	def get_move_diagonals(piece, game, y, x):
		moves = []
		moves += PieceUtils.get_move_north_east(piece, game, y, x)
		moves += PieceUtils.get_move_south_east(piece, game, y, x)
		moves += PieceUtils.get_move_north_west(piece, game, y, x)
		moves += PieceUtils.get_move_south_west(piece, game, y, x)
		return moves

	### --- Single Square NSEW --- ###
	@staticmethod
	def get_move_north(piece, game, y, x):
		return PieceUtils.validate_move(piece, game, y + 1, x)

	@staticmethod
	def get_move_south(piece, game, y, x):
		return PieceUtils.validate_move(piece, game, y - 1, x)

	@staticmethod
	def get_move_east(piece, game, y, x):
		return PieceUtils.validate_move(piece, game, y, x + 1)

	@staticmethod
	def get_move_west(piece, game, y, x):
		return PieceUtils.validate_move(piece, game, y, x - 1)

	### --- Single Square Diagonals --- ###
	@staticmethod
	def get_move_north_west(piece, game, y, x):
		return PieceUtils.validate_move(piece, game, y + 1, x - 1)

	@staticmethod
	def get_move_north_east(piece, game, y, x):
		return PieceUtils.validate_move(piece, game, y + 1, x + 1)

	@staticmethod
	def get_move_south_west(piece, game, y, x):
		return PieceUtils.validate_move(piece, game, y - 1, x - 1)

	@staticmethod
	def get_move_south_east(piece, game, y, x):
		return PieceUtils.validate_move(piece, game, y - 1, x + 1)