WINNING_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

def check_winner(cells, mark):
    for first, second, third in WINNING_LINES:
        if cells[first] == mark and cells[second] == mark and cells[third] == mark:
            return True
    return False

def is_board_full(cells):
    return " " not in cells
