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

    def __str__(self):
        text = []
        line = '+---+---+---+---+---+---+---+'
        for row in self.board:
            text.append(line)
            rep = '| %s | %s | %s | %s | %s | %s | %s |'
            text.append(
                rep % tuple((i if i is not None else ' ') for i in row))
        text.append(line)
        return '\n'.join(text)

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

        # diagonal \
        for i in range(Game.ROWS - 3):
            for j in range(self.COLUMNS - 3):
                if (
                    board[i][j] == board[i + 1][j + 1] == turn and
                    board[i + 2][j + 2] == board[i + 3][j + 3] == turn
                ):
                    return True

        # diagonal /
        for i in range(Game.ROWS - 3):
            for j in range(self.COLUMNS - 1, 2, -1):
                if (
                    board[i][j] == board[i + 1][j - 1] == turn and
                    board[i + 2][j - 2] == board[i + 3][j - 3] == turn
                ):
                    return True

        return False

    def is_valid_move(self, column):
        return (
            0 <= column < self.COLUMNS and
            self.board[0][column] is None
        )

    def make_move(self, column):
        if not self.is_valid_move(column):
            raise ValueError('Invalid move')

        for i in reversed(range(self.ROWS)):
            if self.board[i][column] is None:
                self.board[i][column] = self.turn
                break

        if self.habemus_victor():
            self.winner = self.turn

    def restart(self):
        self.board = [[None] * self.COLUMNS for i in range(self.ROWS)]
        self.turn = 0
        self.winner = None

    def play(self):
        def ask():
            col = int(raw_input('Column: '))
            return col

        while not self.is_over():
            print(self)
            try:
                self.make_move(ask())
            except Exception:
                print 'Invalid move'
                self.make_move(ask())
            self.next_turn()

        if self.winner:
            print('The winner is player: %s' % self.winner)
        else:
            print("Cat's game")

def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
