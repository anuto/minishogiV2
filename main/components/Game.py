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
			return self.turn % 2

		raise Exception("game has already ended :c")

	# map player turn to side
	def get_active_side(self):
		return self.sides[self.turn % 2]

	def make_move(self, start_square, end_square):
		player = side.get_active_side()
		piece = next((piece for piece in player.pieces if piece.square == start_square), None)

	# return map of 'piece'-> [valid squares to move to]
	def get_valid_moves_for_active_player(self):
		player = self.get_active_side()
		moves = {}
		for piece in player.pieces:
			moves[(piece.type, piece.square)] = piece.get_valid_moves(self)
		return moves

	def occupied_by_ally_piece(self, side, square):
		for piece in self.get_active_side().pieces:
			if piece.square == square:
				return True
			return False

	def occupied_by_enemy_piece(self, side, square):
		# 1 % 2 = 1 + 1 = 2
		# 2 % 2 = 0 + 1 = 1
		opposite_side = (side % 2) + 1
		for piece in self.sides[opposite_side].pieces:
			if piece.square == square:
				return True
			return False