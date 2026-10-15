import pandas as pd
import matplotlib.pyplot as plt

# Sample student dataset
data = {
    "Study Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks":       [60, 65, 70, 72, 78, 80, 84, 86, 90, 95]
}
df = pd.DataFrame(data)

print("DAV Lab: Histogram and Scatter Plot")
print("\nDataset:")
print(df.to_string(index=False))

# 1. Histogram of marks
plt.figure(figsize=(7, 4))
plt.hist(df["Marks"], bins=5, edgecolor="black")
plt.title("Histogram of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("histogram.png", dpi=150)
plt.show()

# 2. Scatter plot of study hours vs marks
plt.figure(figsize=(7, 4))
plt.scatter(df["Study Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("scatter_plot.png", dpi=150)
plt.show()

print("\nOutput graphs saved as histogram.png and scatter_plot.png")
