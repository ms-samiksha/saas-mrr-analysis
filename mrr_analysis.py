import pandas as pd
import matplotlib.pyplot as plt

# Quarterly MRR Growth Data (2024)
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "MRR_Growth": [3.58, 5.48, 9.31, 10.77]
}

df = pd.DataFrame(data)

industry_target = 15
avg_growth = df["MRR_Growth"].mean()

print("Average MRR Growth (2024):", round(avg_growth, 2))

plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["MRR_Growth"], marker="o", linewidth=2)
plt.axhline(y=industry_target, linestyle="--", linewidth=2)

plt.title("SaaS MRR Growth Trend (2024)")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth")
plt.tight_layout()
plt.savefig("mrr_growth_trend.png")
plt.show()
