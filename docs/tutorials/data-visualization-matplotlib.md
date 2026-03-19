# Data Visualization with Matplotlib and Seaborn

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Tutorial

Create publication-quality charts and plots for reports and presentations.

## Prerequisites

- Python 3.9+
- Pandas, Matplotlib, Seaborn installed

## Step 1: Install

```bash
pip install matplotlib seaborn pandas numpy
```

## Step 2: Basic Plots

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Line chart
x = np.linspace(0, 10, 100)
plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), label="sin(x)", linewidth=2)
plt.plot(x, np.cos(x), label="cos(x)", linewidth=2)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Trigonometric Functions")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("line_chart.png", dpi=150, bbox_inches="tight")
plt.show()
```

## Step 3: Statistical Plots with Seaborn

```python
# Load sample data
df = sns.load_dataset("tips")

# Distribution plot
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

sns.histplot(data=df, x="total_bill", kde=True, ax=axes[0])
axes[0].set_title("Distribution of Total Bill")

sns.boxplot(data=df, x="day", y="total_bill", ax=axes[1])
axes[1].set_title("Bill by Day")

sns.scatterplot(data=df, x="total_bill", y="tip", hue="smoker", ax=axes[2])
axes[2].set_title("Bill vs Tip")

plt.tight_layout()
plt.savefig("statistical_plots.png", dpi=150)
```

## Step 4: Heatmaps

```python
# Correlation heatmap
correlation = df.select_dtypes(include=[np.number]).corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", center=0)
plt.title("Correlation Matrix")
plt.savefig("heatmap.png", dpi=150, bbox_inches="tight")
```

## Style Guide for Charts

- Always include axis labels and a title
- Use `figsize=(10, 6)` as a default
- Save at 150+ DPI for reports
- Use colorblind-friendly palettes: `sns.set_palette("colorblind")`

---

*Last updated: March 2026 · Author: Arshad Naguru*
