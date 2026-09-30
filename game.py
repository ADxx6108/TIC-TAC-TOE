from board import Board
from players import Player
from rules import check_winner, is_board_full


class TicTacToeGame:
    def __init__(self):
        self.board = Board()
        self.players = [Player("X"), Player("O")]
        self.current = 0

    def play(self):
        print("\nEnter a number from 1 to 9 to place your mark.")

        while True:
            self.board.show()
            player = self.players[self.current]

            move = player.get_move(self.board)
            self.board.place_mark(move, player.mark)

            if check_winner(self.board.cells, player.mark):
                self.board.show()
                print(f"Player {player.mark} wins!")
                player.wins += 1
                break

            if is_board_full(self.board.cells):
                self.board.show()
                print("It is a draw!")
                break

            self.current = 1 - self.current
