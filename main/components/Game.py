from os import sys,path
PARENT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(PARENT_DIR)

from components.Side import Side

class Game(object):
	def __init__(self):
		self.sides = {
			1: None,
			2: None
		}
		self.turn = 1
	
	# param: name should be the string name of the player
	def add_player(self, name):
		for i in range(1, 3):
			if not self.sides[i]:
				self.sides[i] = Side(name, i)
				return
		
		raise Exception("3 is a crowd :c")	

	# returns true if both players are present
	def game_start(self):
		return self.sides[1] and self.sides[2]

	def game_over(self):
		return self.sides[1].lost() or self.sides[2].lost()

	# returns the Player that won if the game is over, otherwise throws an exception
	def winner(self):
		if gameOver():
			return self.sides[2] if self.sides[1].lost() else self.sides[1]
		raise Exception("game is not over!!!")

	# returns the player that's turn it is
	def get_player_turn(self):
		return self.get_active_side().player.name

	# returns the player that's turn it is
	def get_player_number_turn(self):
		if not self.game_over():
			return ((self.turn + 1) % 2) + 1

		raise Exception("game has already ended :c")

	def get_opponent_player_number(self):
		if not self.game_over():
			return self.turn % 2 + 1

		raise Exception("game has already ended :c")

	# map player turn to side
	def get_active_side(self):
		return self.sides[self.get_player_number_turn()]

	def get_opponent_side(self):
		return self.sides[self.get_opponent_player_number()]

	def move_piece(self, start_square, end_square):
		player = self.get_active_side()
		piece = next((piece for piece in player.pieces if piece.square == start_square), None)
		if piece:
			if  end_square in piece.get_valid_moves(self):
				current_enemy_piece = self.square_occupied_by_enemy_piece(piece.side, end_square)
				if current_enemy_piece:
					# remove piece from opponent, should reset any promotion
					opponent_side = self.get_opponent_side()
					opponent_side.piece_captured(current_enemy_piece)

					current_side = self.get_active_side()
					current_side.add_captured(current_enemy_piece)

				piece.move_piece(end_square)
			else:
				raise Exception("piece cannot move there ;c")
		else:
			raise Exception("you have no pieces on the start square? :o")

	def can_promote_piece(self, promote_square):
		pieces = self.get_active_side().pieces
		piece = self.get_piece_on_square(pieces, promote_square)
		return piece and piece.can_promote()

	def promote_piece(self, promote_square):
		pieces = self.get_active_side().pieces
		piece = self.get_piece_on_square(pieces, promote_square)
		if piece:
			if piece.can_promote():
				piece.promote()
				return
			else:
				raise Exception("this piece cannot promote!!")

		raise Exception("no piece selected to promote!!!")

	def end_turn(self):
		self.turn += 1

	# return map of 'piece'-> [valid squares to move to]
	def get_valid_moves_for_active_player(self):
		pieces = self.get_active_side().pieces
		moves = {}
		for piece in pieces:
			moves[(piece.type, piece.square)] = piece.get_valid_moves(self)
		return moves

	def square_occupied_by_ally_piece(self, side, square):
		pieces = self.get_active_side().pieces
		return self.get_piece_on_square(pieces, square)

	def square_occupied_by_enemy_piece(self, side, square):
		pieces = self.get_opponent_side().pieces
		return self.get_piece_on_square(pieces, square)

	def get_piece_on_square(self, pieces, square):
		for piece in pieces:
			if piece.square == square:
				return piece
		return None
