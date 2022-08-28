import sys
sys.path.append('../')
from components.Game import Game

class GameController(object):

	def __init__(self):
		self.game = None

	def start_game(self):
		self.game = Game()

	def add_player(self, name):
		self.game.add_player(name)

	# returns the name of the next player
	def get_player_turn(self):
		return self.game.get_player_turn()

	# taking a start square and a square to move to, does so if the move is legal
	def move_piece(self, start_square, end_square):
		self.game.move_piece(start_square, end_square)

	# taking a piece, places the piece if legal
	def place_piece(self, piece, placement_square):
		self.game.place_piece(piece, placement_square)

	def get_valid_moves_for_active_player(self):
		return self.game.get_valid_moves_for_active_player()