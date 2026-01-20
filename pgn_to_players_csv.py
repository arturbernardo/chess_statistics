import chess.pgn
import csv
from collections import defaultdict

def game_mode(event):
    if "Classical" in event:
        return "Classical"
    if "Blitz" in event:
        return "Blitz"
    if "Rapid" in event:
        return "Rapid"
    if "Bullet" in event:
        return "Bullet"
    return None

stats = defaultdict(lambda: {
    "games": 0,
    "wins": 0,
    "losses": 0,
    "draws": 0,
    "elo_sum": 0
})

with open("input.pgn") as pgn:
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None:
            break

        h = game.headers

        # apenas jogos rated
        event = h.get("Event", "")
        if not event.startswith("Rated"):
            continue

        mode = game_mode(event)
        if mode is None:
            continue

        white = h.get("White")
        black = h.get("Black")

        try:
            white_elo = int(h.get("WhiteElo", 0))
            black_elo = int(h.get("BlackElo", 0))
        except ValueError:
            continue

        result = h.get("Result")

        # White
        key_w = (white, mode)
        stats[key_w]["games"] += 1
        stats[key_w]["elo_sum"] += white_elo

        # Black
        key_b = (black, mode)
        stats[key_b]["games"] += 1
        stats[key_b]["elo_sum"] += black_elo

        if result == "1-0":
            stats[key_w]["wins"] += 1
            stats[key_b]["losses"] += 1
        elif result == "0-1":
            stats[key_b]["wins"] += 1
            stats[key_w]["losses"] += 1
        elif result == "1/2-1/2":
            stats[key_w]["draws"] += 1
            stats[key_b]["draws"] += 1

with open("players_by_mode.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "player",
        "mode",
        "games",
        "wins",
        "losses",
        "draws",
        "avg_elo"
    ])

    for (player, mode), s in stats.items():
        writer.writerow([
            player,
            mode,
            s["games"],
            s["wins"],
            s["losses"],
            s["draws"],
            round(s["elo_sum"] / s["games"], 1)
        ])
