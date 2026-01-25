import chess.pgn
import sys

pgn = open(sys.argv[1])
game_id = 0

while True:
    game = chess.pgn.read_game(pgn)
    if game is None:
        break

    link = game.headers.get("Site", "")
    white = game.headers.get("White", "Unknown")
    black = game.headers.get("Black", "Unknown")

    board = game.board()
    move_number = 0

    for move in game.mainline_moves():
        san = board.san(move)
        uci = move.uci()

        board.push(move)
        move_number += 1

        fen = board.fen()
        
        print(f"{game_id},{move_number},{white},{black},{san},{uci},{fen},{link}")

    game_id += 1
