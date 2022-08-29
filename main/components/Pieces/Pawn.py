from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils
from PromotionUtils import PromotionUtils

class Pawn(Piece):

	SIDE_1_STARTING_SQUARE = (1, 0)
	SIDE_2_STARTING_SQUARE = (3, 4)

	def get_base_type(self):
		return PieceType.PAWN

	def get_promote_type(self):
		return PieceType.PROMOTED_PAWN

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