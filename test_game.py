from game import Game


def test_winning_moves():
    n = None
    board = [
        [n, n, 1, 1, 1, n, n],
        [n, n, n, n, n, n, n],
        [n, n, n, n, n, n, n],
        [n, n, n, n, n, n, n],
        [n, n, n, n, n, n, n],
        [n, n, n, n, n, n, n]
    ]

    game = Game(board=board, turn=1)
    game.make_move(0, 5)
    assert game.habemus_victor()
    assert game.turn == 1
    assert game.winner == 1

    board = [
        [n, n, n, n, n, n, n],
        [n, n, n, n, 1, n, n],
        [n, n, n, 1, n, n, n],
        [n, n, 1, n, n, n, n],
        [n, n, n, n, n, n, n],
        [n, n, n, n, n, n, n]
    ]

    game = Game(board=board, turn=1)
    game.make_move(0, 5)
    assert game.habemus_victor()
    assert game.turn == 1
    assert game.winner == 1

    board = [
        [n, n, 1, n, 1, n, n],
        [n, n, 1, n, n, n, n],
        [n, n, 1, n, n, n, n],
        [n, n, n, n, n, n, n],
        [n, n, n, n, n, n, n],
        [n, n, n, n, n, n, n]
    ]

    game = Game(board=board, turn=1)
    game.make_move(3, 2)
    assert game.habemus_victor()
    assert game.turn == 1
    assert game.winner == 1
