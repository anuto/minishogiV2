from os import sys,path
PARENT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(PARENT_DIR)

from controller.GameController import *

class GameClient:

	def main():
		controller = GameController()

		controller.start_game()
		controller.add_player("Fionna")
		controller.add_player("Marshall")

		turn = controller.get_player_turn()
		print('turn 1: ' + str(turn))

		legal_moves = controller.get_valid_moves_for_active_player()
		print('valid moves players 1')
		for piece, moves in legal_moves.items():
			(name, square) = piece
			print(name.value + ''.join(str(piece)) + ': ' + str(moves))\

		controller.game.turn += 1

		linebreak = ''
		for i in range(100):
			linebreak += '.'
		print(linebreak)

		legal_moves = controller.get_valid_moves_for_active_player()
		print('valid moves player 2')
		for piece, moves in legal_moves.items():
			(name, square) = piece
			print(name.value + ''.join(str(piece)) + ': ' + str(moves))

		linebreak = ''
		for i in range(100):
			linebreak += '='
		print(linebreak)


	if __name__ == "__main__":
	    main()