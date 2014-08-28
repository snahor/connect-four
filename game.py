import pprint


class Game(object):
    ROWS = 6
    COLUMNS = 7

    def __init__(self, turn=0, board=None):
        # create a board of 7 cols x 6 rows
        if not board:
            board = [[None] * self.COLUMNS for i in range(self.ROWS)]
        self.board = board
        self.turn = turn
        self.winner = None

    def is_over(self):
        return self.winner is not None or self.board_is_full()

    def board_is_full(self):
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True

    def next_turn(self):
        """Swap turns"""
        self.turn = 1 >> self.turn

    def habemus_victor(self):
        """Check if user has won the game"""
        turn = self.turn
        board = self.board

        # horizontal
        for row in board:
            for i in range(self.COLUMNS - 3):
                if row[i] == row[i + 1] == row[i + 2] == row[i + 3] == turn:
                    return True

        # vertical
        for j in range(self.COLUMNS):
            for i in range(self.ROWS - 3):
                if (
                    board[i][j] == board[i + 1][j] == turn and
                    board[i + 2][j] == board[i + 3][j] == turn
                ):
                    return True

        # diagonal
        for i in range(self.COLUMNS - 3):
            for j in range(3, self.ROWS):
                if (
                    board[i][j] == board[i + 1][j - 1] == turn and
                    board[i + 2][j - 2] == board[i + 3][j - 3] == turn
                ) or (
                    board[i][j] == board[i + 1][j + 1] == turn and
                    board[i + 2][j + 2] == board[i + 3][j + 3] == turn
                ):
                    return True

        return False

    def is_valid_move(self, row, column):
        return (
            0 <= row < self.ROWS and
            0 <= column < self.COLUMNS and
            self.board[row][column] is None
        )

    def make_move(self, row, column):
        if not self.is_valid_move(row, column):
            raise ValueError('Invalid move')

        self.board[row][column] = self.turn

        if self.habemus_victor():
            self.winner = self.turn

    def restart(self):
        self.board = [[None] * self.COLUMNS for i in range(self.ROWS)]
        self.turn = 0
        self.winner = None

    def play(self):
        def ask():
            row = int(raw_input('row: '))
            col = int(raw_input('col: '))
            return row, col

        while not self.is_over():
            pprint.pprint(self.board)
            try:
                self.make_move(*ask())
            except Exception as exc:
                print 'Invalid move'
                print exc
                self.make_move(*ask())
            self.next_turn()

        print 'winner', self.winner


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
