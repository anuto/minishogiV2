from PieceUtils import PieceUtils

class PromotionUtils:

	@staticmethod
	def get_gold_general_moves(piece, game):
		(y, x) = piece.square
		potential_moves = []

		potential_moves += PieceUtils.get_move_nsew(piece, game, y, x)	

		if piece.side == 1:
			potential_moves += PieceUtils.get_move_north_east(piece, game, y, x)	
			potential_moves += PieceUtils.get_move_north_west(piece, game, y, x)	

		else:
			potential_moves += PieceUtils.get_move_south_east(piece, game, y, x)	
			potential_moves += PieceUtils.get_move_south_west(piece, game, y, x)	

		return potential_moves