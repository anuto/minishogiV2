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

	def get_valid_moves_for_active_player(self):
		return self.game.get_valid_moves_for_active_player()

	# taking a start square and a square to move to, does so if the move is legal
	def move_piece(self, start_square, end_square, should_promote = True):
		self.game.move_piece(start_square, end_square)

		if should_promote and self.game.can_promote_piece(end_square):
			self.game.promote_piece(end_square)

		self.game.end_turn()

	# taking a piece, places the piece if legal
	def place_piece(self, piece, placement_square):
		self.game.place_piece(piece, placement_square)
		# no promotion component, cannot place promotion
		self.game.end_turn()

	def get_captured_pieces_for_active_player(self):
		return self.game.get_captured_pieces_for_active_player()
