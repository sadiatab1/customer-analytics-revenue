import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

np.random.seed(42)

months = pd.date_range(start="2024-01-01", end="2024-12-01", freq="MS")
segments = ["Premium", "Standard", "Budget"]

data = []
for seg in segments:
    base = np.linspace(100, 200, len(months))
    seasonal = 20 * np.sin(np.linspace(0, 2 * np.pi, len(months)))
    noise = np.random.normal(0, 10, len(months))
    multiplier = {"Premium": 1.5, "Standard": 1.0, "Budget": 0.7}[seg]
    revenue = (base + seasonal + noise) * multiplier
    for m, r in zip(months, revenue):
        data.append([m, seg, r])

df = pd.DataFrame(data, columns=["Month", "Segment", "Revenue"])

sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 8))
sns.lineplot(data=df, x="Month", y="Revenue", hue="Segment", marker="o", palette="deep")
plt.title("Monthly Revenue Trends by Customer Segment", fontsize=16, weight="bold")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)

plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

print("✅ Chart saved at:", os.path.abspath("chart.png"))
