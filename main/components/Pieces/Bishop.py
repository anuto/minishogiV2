from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils

class Bishop(Piece):
	def __init__(self, side):
		Piece.__init__(self, side)
		self.type = PieceType.BISHOP
		self.square = PieceUtils.assign_based_on_side(side,
		 (0, 3), 
		 (4, 1)
		)