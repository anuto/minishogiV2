from Piece import Piece
from PieceType import PieceType
from PieceUtils import PieceUtils

class Emperor(Piece):
	def __init__(self, side):
		Piece.__init__(self, side)
		self.type = PieceType.EMPEROR
		self.square = PieceUtils.assign_based_on_side(side,
		 (0, 0), 
		 (4, 4)
		 )