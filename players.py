class Player:
    def __init__(self, mark):
        self.mark = mark
        self.wins = 0

    def get_move(self, board):
        while True:
            choice = input(f"Player {self.mark}, choose a position (1-9): ").strip()

            if not choice.isdigit():
                print("Please enter a number.")
                continue

            position = int(choice)

            if position < 1 or position > 9:
                print("Choose a number between 1 and 9.")
                continue

            if not board.is_empty(position):
                print("That position is already taken.")
                continue

            return position
