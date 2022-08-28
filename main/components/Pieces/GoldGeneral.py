from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils
from PromotionUtils import PromotionUtils

class GoldGeneral(Piece):
	def __init__(self, side):
		Piece.__init__(self, side)
		self.type = PieceType.GOLD_GENERAL
		self.square = PieceUtils.assign_based_on_side(side,
		 (0, 1), 
		 (4, 3)
		 )

	def get_valid_moves(self, game):
		PromotionUtils.get_gold_general_moves(self, game)

	def can_promote(self):
		return False

	def promote(self):
		raise Exception("why are u trying to promote the gold general D:")