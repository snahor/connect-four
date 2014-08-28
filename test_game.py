import pytest
from game import Game

n = None


@pytest.mark.parametrize('board,move,turn', (
    ([[n, n, n, n, n, n, n],
      [n, n, n, n, n, n, n],
      [n, n, n, n, n, n, n],
      [n, 1, 0, n, n, n, n],
      [n, 1, 0, n, n, n, n],
      [n, 1, 0, n, n, n, n]], 2, 0
     ),
    ([[n, n, n, n, n, n, n],
      [n, n, n, n, 0, n, n],
      [1, n, n, 1, 0, 0, n],
      [0, n, n, 0, 0, 1, n],
      [0, n, n, 1, 1, 0, 1],
      [0, n, n, 1, 0, 1, 1]], 4, 0
     ),
    ([[n, n, n, n, n, n, n],
      [n, n, n, 1, n, n, n],
      [n, n, 0, 0, n, n, n],
      [n, 1, 0, 0, n, n, n],
      [1, 1, 1, 0, 0, n, n],
      [0, 0, 1, 1, 1, n, n]], 5, 0
     ),
    ([[n, n, n, n, n, n, n],
      [n, n, n, n, n, n, n],
      [n, n, n, n, n, n, n],
      [n, 1, 0, n, n, n, n],
      [n, 1, 0, n, n, n, n],
      [n, 1, 0, n, n, n, n]], 2, 0
     ),
))
def test_winning_moves(board, move, turn):
    game = Game(board=board, turn=turn)
    assert game.turn == turn
    assert game.is_valid_move(move)
    game.make_move(move)
    assert game.habemus_victor()
    assert game.winner == turn


@pytest.mark.parametrize('board,move,turn', (
    ([[0, n, 1, 1, 0, 1, 0],
      [0, 1, 1, 0, 0, 0, 1],
      [1, 0, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 0, 1, 1],
      [1, 0, 0, 1, 1, 0, 1],
      [0, 1, 1, 0, 0, 0, 1]], 1, 1
     ),
))
def test_cats_game(board, move, turn):
    game = Game(board=board, turn=turn)
    game.make_move(move)
    assert game.is_over()
    assert not game.habemus_victor()
