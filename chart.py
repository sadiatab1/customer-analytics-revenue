import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

# Generate synthetic data
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

# Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create figure **exactly 512x512 pixels**
fig = plt.figure(figsize=(8, 8), dpi=64)  # 8*64=512
ax = fig.add_subplot(111)

sns.lineplot(data=df, x="Month", y="Revenue", hue="Segment", marker="o", palette="deep", ax=ax)

# Titles and labels
ax.set_title("Monthly Revenue Trends by Customer Segment", fontsize=16, weight="bold")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue ($)")
plt.setp(ax.get_xticklabels(), rotation=45)  # rotate x-axis labels

# Save exactly 512x512 **without bbox_inches**
fig.savefig("chart.png", dpi=64)  # DO NOT use bbox_inches='tight'
plt.close()
