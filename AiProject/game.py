from board import Board
import time
import random

# GAME LINK
# http://kevinshannon.com/connect4/

EMPTY = 0
RED = 1
BLUE = 2


def main():
    board = Board()
    time.sleep(3)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        
        # FOR DEBUG PURPOSES
        board.print_grid(game_board)
        print("\n")
        if game_end:
            break
        # YOUR CODE GOES HER
        column,_ = board.minimax(game_board,4,RED)
        print("best of the best" , column)
        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        board.select_column(column)

        time.sleep(2)


if __name__ == "__main__":
    main()