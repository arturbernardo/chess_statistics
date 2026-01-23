import chess
import chess.engine
import csv
import sys
import time

STOCKFISH_PATH = "/usr/bin/stockfish"
DEPTH = 18

engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

writer = csv.writer(sys.stdout)
writer.writerow(["game", "move", "depth", "score_cp", "nodes", "time_ms"])

reader = csv.reader(sys.stdin)

for game_id, move_number, fen in reader:
    board = chess.Board(fen)

    start = time.time()
    info = engine.analyse(
        board,
        chess.engine.Limit(depth=DEPTH)
    )
    elapsed_ms = int((time.time() - start) * 1000)

    score = info["score"].pov(board.turn).score(mate_score=10000)

    depth = info.get("depth", DEPTH)
    nodes = info.get("nodes", 0)

    writer.writerow([
        game_id,
        move_number,
        depth,
        score,
        nodes,
        elapsed_ms
    ])

engine.quit()
