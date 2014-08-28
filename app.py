import json
from bottle import run, route, post, request, HTTPResponse, template
from game import Game

game = Game()


def error(msg):
    return _json({'error': msg}, status=400)


def _json(data, status=200):
    return HTTPResponse(
        status=status,
        content_type='application/json',
        body=json.dumps(data)
    )


@route('/user/<turn:re:[1,2]>')
@route('/users/<turn:re:[1,2]>')
def index(turn):
    colors = ['red', 'blue']
    turn = int(turn) - 1
    return template(
        'board.html',
        board=json.dumps(game.board),
        turn=turn,
        color=colors[turn]
    )


@post('/user/<turn:re:[1,2]>/move')
@post('/users/<turn:re:[1,2]>/move')
def move(turn):
    turn = int(turn) - 1

    if turn != game.turn:
        return error("You can't make a move, wait for your opponent.")

    try:
        game.make_move(int(request.forms.get('column')))
        game.next_turn()
        return game_state()
    except ValueError as exc:
        return error(exc)


@route('/state')
def game_state():
    return _json({
        'board': game.board,
        'winner': game.winner,
        'turn': game.turn,
    })


@route('/restart')
def restart():
    game.restart()
    return game_state()


run(host='localhost', port=8888, debug=True, reloader=True)
