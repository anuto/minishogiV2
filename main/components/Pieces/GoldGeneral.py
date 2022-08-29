from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils
from PromotionUtils import PromotionUtils

class GoldGeneral(Piece):

	SIDE_1_STARTING_SQUARE = (0, 1)
	SIDE_2_STARTING_SQUARE = (4, 3)
	
	def get_base_type(self):
		return PieceType.GOLD_GENERAL

	def get_promote_type(self):
		raise Exception("gold general has no promote type, does not promote")

	def get_valid_moves(self, game):
		return PromotionUtils.get_gold_general_moves(self, game)

	def can_promote(self):
		return False

	def promote(self):
		raise Exception("why are u trying to promote the gold general D:")