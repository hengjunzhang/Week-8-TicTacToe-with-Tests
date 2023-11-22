import random

class TicTacToe:
    def __init__(self, single_player=False):
        self.board = self.get_empty_board()
        self.current_player = 'X'
        self.single_player = single_player
        self.bot = 'O' if single_player else None

    def get_empty_board(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def print_board(self):
        for row in self.board:
            print([cell if cell is not None else ' ' for cell in row])


    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_player_input(self):
        if self.current_player == self.bot:
            empty_positions = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]
            return random.choice(empty_positions)
        else:
            prompt = f"player {self.current_player} > "
            player_input = input(prompt)
            row_col_list = player_input.split(',')
            return [int(x) for x in row_col_list]

    def check_winner(self):
        for row in self.board:
            if len(set(row)) == 1 and row[0] is not None:
                return row[0]

        for i in range(3):
            column = [self.board[j][i] for j in range(3)]
            if len(set(column)) == 1 and column[0] is not None:
                return self.board[0][i]

        top_left_to_bottom_right = [self.board[i][i] for i in range(3)]
        if len(set(top_left_to_bottom_right)) == 1 and top_left_to_bottom_right[0] is not None:
            return self.board[0][0]

        top_right_to_bottom_left = [self.board[i][2-i] for i in range(3)]
        if len(set(top_right_to_bottom_left)) == 1 and top_right_to_bottom_left[0] is not None:
            return self.board[0][2]

        if all(cell is not None for row in self.board for cell in row):
            return "draw"

        return None

    def play_game(self):
        winner = None
        while winner is None:
            self.print_board()
            try:
                row, col = self.get_player_input()
                if self.board[row][col] is not None:
                    print("Spot taken, try again")
                    continue
            except (ValueError, IndexError):
                print("Invalid input, try again.")
                continue

            self.board[row][col] = self.current_player
            winner = self.check_winner()
            self.switch_player()

        self.print_board()
        if winner == "draw":
            print("Draw")
        elif winner:
            print(f"winner is {winner}")
