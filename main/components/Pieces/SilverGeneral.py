from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils

class SilverGeneral(Piece):

	SIDE_1_STARTING_SQUARE = (0, 2)
	SIDE_2_STARTING_SQUARE = (4, 2)

	def get_valid_moves(self, game):
		if self.is_promoted:
			return PromotionUtils.get_gold_general_moves(self, game)
		else:
			(y, x) = self.square
			potential_moves = []

			potential_moves += PieceUtils.get_move_diagonals(self, game, y, x)

			if self.side == 1:
				potential_moves += PieceUtils.get_move_north(self, game, y, x)	
			else:
				potential_moves += PieceUtils.get_move_south(self, game, y, x)	

			return potential_moves

	def get_base_type(self):
		return PieceType.SILVER_GENERAL

	def get_promote_type(self):
		return PieceType.PROMOTED_SILVER_GENERAL