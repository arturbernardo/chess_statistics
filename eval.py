import chess
import chess.engine
import csv
import sys
import time
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

STOCKFISH_PATH = "/usr/games/stockfish"
DEPTH = 18
WORKERS = max(1, cpu_count() - 1)

def init_engine():
    global engine
    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
    engine.configure({
        "Threads": 1,
        "Hash": 256
    })

def analyse_row(row):
    game_id, move_number, white, black, fen = row
    board = chess.Board(fen)

    t0 = time.time()
    info = engine.analyse(board, chess.engine.Limit(depth=DEPTH))
    t1 = time.time()

    score = info["score"].pov(board.turn).score(mate_score=10000)

    return [
        game_id,
        move_number,
        white,
        black,
        info.get("depth", DEPTH),
        score,
        info.get("nodes", 0),
        int((t1 - t0) * 1000)
    ]

def main():
    reader = csv.reader(sys.stdin)
    rows = list(reader)

    writer = csv.writer(sys.stdout)
    writer.writerow([
        "game",
        "move",
        "white",
        "black",
        "depth",
        "score_cp",
        "nodes",
        "time_ms"
    ])

    with Pool(
        processes=WORKERS,
        initializer=init_engine
    ) as pool:
        for result in tqdm(
            pool.imap_unordered(analyse_row, rows),
            total=len(rows),
            file=sys.stderr
        ):
            writer.writerow(result)

if __name__ == "__main__":
    main()
