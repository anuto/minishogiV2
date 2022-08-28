from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils

class GoldGeneral(Piece):
	def __init__(self, side):
		Piece.__init__(self, side)
		self.type = PieceType.GOLD_GENERAL
		self.square = PieceUtils.assign_based_on_side(side,
		 (0, 1), 
		 (4, 3)
		 )