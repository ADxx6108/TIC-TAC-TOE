from game import TicTacToeGame


def main():
    print("=== TIC-TAC-TOE ===")
    print("Player X and Player O will take turns.")

    while True:
        game = TicTacToeGame()
        game.play()

        again = input("\nPlay another game? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
