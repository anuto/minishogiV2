class Piece():
	def __init__(self, side):
		self.type = None
		self.square = (-1, -1)
		self.side = side
		self.is_promoted = False

	def get_valid_moves(self, game):
		raise Exception("valid moves should be overwritten")

	def move_piece(self, end_square):
		self.square = end_square

	def can_promote(self):
		if self.side == 1:
			return self.square[0] == 4 and not self.is_promoted
		else:
			return self.square[0] == 0 and not self.is_promoted

	def promote(self):
		self.is_promoted = True

	def captured(self):
		self.is_promoted = False