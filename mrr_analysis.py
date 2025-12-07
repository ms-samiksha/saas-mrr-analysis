# SaaS MRR Growth Analysis
# Email: 23f3001448@ds.study.iitm.ac.in

import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------
# 1. Define the quarterly data
# -----------------------------
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "MRR_Growth": [3.58, 5.48, 9.31, 10.77]
}

industry_target = 15  # benchmark target

df = pd.DataFrame(data)

# -----------------------------
# 2. Calculate average MRR growth
# -----------------------------
average_growth = df["MRR_Growth"].mean()
print("Average MRR Growth:", round(average_growth, 2))

# -----------------------------
# 3. Plot the MRR trend + benchmark
# -----------------------------
plt.figure(figsize=(8, 5))

# Line plot of quarterly MRR growth
plt.plot(df["Quarter"], df["MRR_Growth"], marker="o", label="Company MRR Growth")

# Benchmark line
plt.axhline(industry_target, color="red", linestyle="--", label="Industry Target (15)")

# Annotations
for i, val in enumerate(df["MRR_Growth"]):
    plt.text(i, val + 0.3, f"{val}", ha="center", fontsize=9)

plt.title("2024 Quarterly MRR Growth vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth (%)")
plt.ylim(0, max(df["MRR_Growth"].max(), industry_target) + 2)
plt.legend()
plt.tight_layout()

# Save the chart
plt.savefig("mrr_growth_trend.png")
plt.close()
