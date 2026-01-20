import glob
import re

print("game,move,depth,score,nodes,time")

for f in glob.glob("uci/*.out"):
    with open(f) as fh:
        last_info = None
        for line in fh:
            if line.startswith("info depth"):
                last_info = line

    if not last_info:
        continue

    m = re.search(
        r"depth (\d+).*score (cp|mate) (-?\d+).*nodes (\d+).*time (\d+)",
        last_info
    )

    if not m:
        continue

    game, move = re.search(r"g(\d+)_m(\d+)", f).groups()
    depth, stype, score, nodes, time = m.groups()

    if stype == "mate":
        score = 100000 if int(score) > 0 else -100000

    print(f"{game},{move},{depth},{score},{nodes},{time}")
