from enum import Enum
import random

class ThreeDTicTacToe:
    class CellValue(Enum):
        X = "X"
        O = "O"
        EMPTY = " "  # Represents an empty cell

    def __init__(self):
        # Initialize the 4x4x4 board with EMPTY cells
        self.board = [[[self.CellValue.EMPTY for _ in range(4)] for _ in range(4)] for _ in range(4)]
        self.current_player = self.CellValue.X  # Default starting player
        self.play_with_computer = False
        self.computer_starts = False

    def display_board(self):
        # Display the current state of the board layer by layer
        for layer in range(4):
            print(f"Layer {layer + 1}:")
            for row in self.board[layer]:
                print(" | ".join(cell.value for cell in row))
            print("-" * 17)  # Separator between rows

    def make_move(self, layer, row, col):
        # Validate and make a move on the board
        if self.board[layer][row][col] != self.CellValue.EMPTY:
            print("Cell is already occupied. Try again.")
            return False
        self.board[layer][row][col] = self.current_player
        return True

    def computer_move(self):
        # Simple AI: Randomly choose an empty cell
        empty_cells = [
            (layer, row, col)
            for layer in range(4)
            for row in range(4)
            for col in range(4)
            if self.board[layer][row][col] == self.CellValue.EMPTY
        ]
        if empty_cells:
            layer, row, col = random.choice(empty_cells)
            self.board[layer][row][col] = self.current_player

    def check_winner(self):
        # Check rows, columns, layers, and diagonals for a winner
        for layer in range(4):
            for i in range(4):
                # Check rows
                if self.board[layer][i][0] == self.board[layer][i][1] == self.board[layer][i][2] == self.board[layer][i][3] != self.CellValue.EMPTY:
                    return self.board[layer][i][0]
                # Check columns
                if self.board[layer][0][i] == self.board[layer][1][i] == self.board[layer][2][i] == self.board[layer][3][i] != self.CellValue.EMPTY:
                    return self.board[layer][0][i]

        # Check vertical columns through layers
        for row in range(4):
            for col in range(4):
                if (
                    self.board[0][row][col] == self.board[1][row][col] == self.board[2][row][col] == self.board[3][row][col] != self.CellValue.EMPTY
                ):
                    return self.board[0][row][col]

        # Check main diagonals within each layer
        for layer in range(4):
            if (
                self.board[layer][0][0] == self.board[layer][1][1] == self.board[layer][2][2] == self.board[layer][3][3] != self.CellValue.EMPTY
                or self.board[layer][0][3] == self.board[layer][1][2] == self.board[layer][2][1] == self.board[layer][3][0] != self.CellValue.EMPTY
            ):
                return self.board[layer][0][0]

        # Check cross-layer diagonals
        if (
            self.board[0][0][0] == self.board[1][1][1] == self.board[2][2][2] == self.board[3][3][3] != self.CellValue.EMPTY
            or self.board[0][3][3] == self.board[1][2][2] == self.board[2][1][1] == self.board[3][0][0] != self.CellValue.EMPTY
        ):
            return self.board[0][0][0]

        return None

    def is_draw(self):
        # Check if the game is a draw (no empty cells left)
        return all(
            cell != self.CellValue.EMPTY for layer in self.board for row in layer for cell in row
        )

    def switch_player(self):
        # Switch turns between players
        self.current_player = self.CellValue.O if self.current_player == self.CellValue.X else self.CellValue.X

    def play_game(self):
        # Choose game mode
        print("Welcome to 3D Tic-Tac-Toe!")
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

        # Main game loop
        self.display_board()

        while True:
            if self.play_with_computer and (
                (self.computer_starts and self.current_player == self.CellValue.X) or
                (not self.computer_starts and self.current_player == self.CellValue.O)
            ):
                print("Computer's turn:")
                self.computer_move()
            else:
                try:
                    print(f"{self.current_player.value}'s turn. Enter layer, row, and column (0-3):")
                    layer, row, col = map(int, input().split())

                    if layer < 0 or layer > 3 or row < 0 or row > 3 or col < 0 or col > 3:
                        print("Invalid input. Please enter numbers between 0 and 3.")
                        continue

                    # Make the move
                    if not self.make_move(layer, row, col):
                        continue

                except ValueError:
                    print("Invalid input. Please enter three numbers separated by spaces.")
                    continue

            self.display_board()

            # Check for a winner
            winner = self.check_winner()
            if winner:
                print(f"{winner.value} wins!")
                break

            # Check for a draw
            if self.is_draw():
                print("It's a draw!")
                break

            # Switch to the other player
            self.switch_player()

if __name__ == "__main__":
    game = ThreeDTicTacToe()
    game.play_game()
