import chess.pgn
import sys

pgn = open(sys.argv[1])
game_id = 0

while True:
    game = chess.pgn.read_game(pgn)
    if game is None:
        break

    board = game.board()
    move_number = 0

    for move in game.mainline_moves():
        board.push(move)
        move_number += 1
        print(f"{game_id},{move_number},{board.fen()}")

    game_id += 1
