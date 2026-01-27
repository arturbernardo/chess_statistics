import pandas as pd
import matplotlib.pyplot as plt

bins = [0, 5, 10, 20, 50, 100, 200, 500, 10_000]
labels = ["0-5", "6-10", "11-20", "21-50", "51-100", "101-200", "201-500", "500+"]

df = pd.read_csv("examples/analysis.csv")

df["cpl_bin"] = pd.cut(df["cpl"], bins=bins, labels=labels, right=True)
counts = df["cpl_bin"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
counts.plot(kind="bar")

plt.xlabel("CPL range")
plt.ylabel("Number of moves")
plt.title("CPL distribution")

plt.tight_layout()
plt.savefig("server/cpl_distribution.png", dpi=150)
plt.close()