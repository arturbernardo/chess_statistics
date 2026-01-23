import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("/usr/bin/stockfish")

board = chess.Board(fen)

info = engine.analyse(
    board,
    chess.engine.Limit(depth=18)
)

cp = info["score"].pov(board.turn).score(mate_score=10000)

engine.quit()
