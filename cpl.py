import sys
import csv

def clamp(cp, limit=1000):
    return max(-limit, min(limit, cp))

rows = list(csv.DictReader(sys.stdin))

fieldnames = list(rows[0].keys()) + ["cpl"] + ["is_white"]
out = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
out.writeheader()

for i, row in enumerate(rows):
    move = int(row["move"])
    is_white = move % 2 == 1
    sign = 1 if is_white else -1

    # Eval before is zero if it is the first move
    if move == 1:
        eval_before = 0
    else:
        eval_before = clamp(int(rows[i-1]["score_cp"]))

    eval_after  = clamp(int(row["score_cp"]))

    cpl = max(0, (eval_before - eval_after) * sign)

    row["cpl"] = cpl
    row["is_white"] = is_white
    out.writerow(row)
