class PieceUtils:
	
	@staticmethod
	def assign_based_on_side(side, option_1, option_2):
		return option_1 if side == 1 else option_2