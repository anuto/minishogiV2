from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils
from PromotionUtils import PromotionUtils

class Pawn(Piece):
	def __init__(self, side):
		Piece.__init__(self, side)
		self.type = PieceType.PAWN
		self.square = PieceUtils.assign_based_on_side(side,
		 (1, 0), 
		 (3, 4)
		 )

	def get_valid_moves(self, game):
		if self.is_promoted:
			return PromotionUtils.get_gold_general_moves(self, game)
		else:
			(y, x) = self.square

			if self.side == 1:
				return PieceUtils.get_move_north(self, game, y, x)	

			else:
				return PieceUtils.get_move_south(self, game, y, x)	

	# pawns are required to promote due to having no other legal moves otherwise
	def move_piece(self, end_square):
		self.square = end_square
		if self.can_promote():
			self.promote()