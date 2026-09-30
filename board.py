class Board:
    def __init__(self):
        self.cells = [" "] * 9

    def show(self):
        print()
        print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]}     1 | 2 | 3")
        print("---+---+---     ---+---+---")
        print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]}     4 | 5 | 6")
        print("---+---+---     ---+---+---")
        print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]}     7 | 8 | 9")
        print()

    def place_mark(self, position, mark):
        self.cells[position - 1] = mark

    def is_empty(self, position):
        return self.cells[position - 1] == " "
