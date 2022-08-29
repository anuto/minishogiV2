class Piece():
	def __init__(self, side):
		self.type = self.get_base_type()
		self.side = side
		self.is_promoted = False
		if side == 1:
			self.square = self.SIDE_1_STARTING_SQUARE
		else:
			self.square = self.SIDE_2_STARTING_SQUARE

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
		self.type = self.get_promote_type()

	def captured(self):
		self.is_promoted = False
		self.type = self.get_base_type()

	def get_base_type(self):
		raise Exception("base type should be specified on each piece")

	def get_promote_type(self):
		raise Exception("promote type should be specified on each piece")