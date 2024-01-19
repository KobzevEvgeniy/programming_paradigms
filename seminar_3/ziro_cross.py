import random


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        print(self.board)

    def move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            self.print_board()
            winner = self.check_winner()
            if winner:
                print(f"The winner is: {winner}")
                return True
            elif " " not in self.board:
                print("It's a draw!")
                return True
            else:
                # Ход компьютера
                self.computer_move()
                winner = self.check_winner()
                if winner:
                    print(f"The winner is: {winner}")
                    return True
                elif " " not in self.board:
                    print("It's a draw!")
                    return True
        else:
            print("The place is occupied")

    def computer_move(self):
        available_positions = [i for i, val in enumerate(self.board) if val == " "]
        if available_positions:
            computer_position = random.choice(available_positions)
            self.board[computer_position] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            print(f"Computer moved to position {computer_position}")
            self.print_board()

    def check_winner(self):
        winner_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for line in winner_positions:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return self.board[line[0]]
        return None

    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            if i < 6:
                print("-" * 9)


