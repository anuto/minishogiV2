from os import sys,path
PARENT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(PARENT_DIR)

from controller.GameController import *

def main():
	controller = GameController()

	controller.start_game()
	controller.add_player("Fionna")
	controller.add_player("Marshall")

	
	print_turn(controller)
	render_moves(controller)

	# controller.game.turn += 1
	controller.move_piece((0, 4), (1, 4))

	linebreak('.')

	print_turn(controller)
	render_moves(controller)

	controller.move_piece((3, 4), (2, 4))
	linebreak('.')

	print_turn(controller)
	render_moves(controller)

	linebreak('=')

def print_turn(controller):
	turn = controller.get_player_turn()
	print('turn: ' + str(turn))

def render_moves(controller):
	legal_moves = controller.get_valid_moves_for_active_player()
	print("valid moves: ")
	for piece, moves in legal_moves.items():
		(name, square) = piece
		print(name.value + ''.join(str(piece)) + ': ' + str(moves))

def linebreak(char_type):
	linebreak = ''
	for i in range(100):
		linebreak += char_type
	print(linebreak)


if __name__ == "__main__":
    main()