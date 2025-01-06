from enum import Enum
import random

class TicTacToe:
    class CellValue(Enum):
        X = "X"
        O = "O"
        EMPTY = " "

    def __init__(self):
        self.board = [[self.CellValue.EMPTY for _ in range(3)] for _ in range(3)]
        self.current_player = self.CellValue.X
        self.play_with_computer = False
        self.computer_starts = False

    def display_board(self):
        for row in self.board:
            print(" | ".join(cell.value for cell in row))
            print("-" * 9)

    def make_move(self, row, col):
        if self.board[row][col] != self.CellValue.EMPTY:
            print("Cell is already occupied. Try again.")
            return False
        self.board[row][col] = self.current_player
        return True

    def computer_move(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == self.CellValue.EMPTY:
                    self.board[row][col] = self.current_player
                    return

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != self.CellValue.EMPTY:
                return row[0]

        for col in range(3):
            if (
                self.board[0][col] == self.board[1][col] == self.board[2][col] != self.CellValue.EMPTY
            ):
                return self.board[0][col]

        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] != self.CellValue.EMPTY
            or self.board[0][2] == self.board[1][1] == self.board[2][0] != self.CellValue.EMPTY
        ):
            return self.board[1][1]

        return None

    def is_draw(self):
        return all(cell != self.CellValue.EMPTY for row in self.board for cell in row)

    def switch_player(self):
        self.current_player = self.CellValue.O if self.current_player == self.CellValue.X else self.CellValue.X

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Choose game mode:")
        print("1. Play against computer")
        print("2. Play with a partner")

        while True:
            try:
                choice = int(input("Enter 1 or 2: "))
                if choice == 1:
                    self.play_with_computer = True
                    break
                elif choice == 2:
                    self.play_with_computer = False
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if self.play_with_computer:
            print("Who plays first?")
            print("1. Player")
            print("2. Computer")

            while True:
                try:
                    first_choice = int(input("Enter 1 or 2: "))
                    if first_choice == 1:
                        self.computer_starts = False
                        self.current_player = self.CellValue.X
                        break
                    elif first_choice == 2:
                        self.computer_starts = True
                        self.current_player = self.CellValue.X
                        break
                    else:
                        print("Invalid choice. Please enter 1 or 2.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            print("Who plays first?")
            print("1. Player 1 (X)")
            print("2. Player 2 (O)")

            while True:
                try:
                    first_choice = int(input("Enter 1 or 2: "))
                    if first_choice == 1:
                        self.current_player = self.CellValue.X
                        break
                    elif first_choice == 2:
                        self.current_player = self.CellValue.O
                        break
                    else:
                        print("Invalid choice. Please enter 1 or 2.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        self.display_board()

        while True:
            if self.play_with_computer and self.computer_starts and self.current_player == self.CellValue.X:
                print("Computer's turn:")
                self.computer_move()
            elif self.play_with_computer and not self.computer_starts and self.current_player == self.CellValue.O:
                print("Computer's turn:")
                self.computer_move()
            else:
                try:
                    print(f"{self.current_player.value}'s turn. Enter row and column (0, 1, 2):")
                    row, col = map(int, input().split())

                    if row < 0 or row > 2 or col < 0 or col > 2:
                        print("Invalid input. Please enter row and column as numbers between 0 and 2.")
                        continue

                    if not self.make_move(row, col):
                        continue

                except ValueError:
                    print("Invalid input. Please enter two numbers separated by a space.")
                    continue

            self.display_board()

            winner = self.check_winner()
            if winner:
                print(f"{winner.value} wins!")
                break

            if self.is_draw():
                print("It's a draw!")
                break

            self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
