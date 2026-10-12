import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    "student": ["sriram", "siva", "naveen", "sriraghu", "ganesh",
                "sudharsan", "vishnu", "venu", "hari", "karthik"],
    "math": [92, 93, 95, 97, 91, 100, 64, 88, 27, 96],
    "science": [90, 98, 96, 93, 100, 55, 74, 96, 36, 95],
    "english": [56, 55, 44, 88, 97, 96, 64, 45, 36, 85],
    "age": [18, 17, 19, 20, 16, 19, 19, 20, 16, 20],
    "hours_studied": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
}
df = pd.DataFrame(data)
print(df)
plt.figure(figsize=(10, 5))
plt.plot(
    df["student"],
    df["math"],
    marker="o",
    label="Math",
    color="blue"
)
plt.plot(
    df["student"],
    df["science"],
    marker="s",
    label="Science",
    color="green"
)
plt.plot(
    df["student"],
    df["english"],
    marker="^",
    label="English",
    color="red"
)
plt.title("Student Score Trends", fontsize=14)
plt.xlabel("Student")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("line_chart.png", dpi=150)
plt.show()
subjects = ["Math", "Science", "English"]
averages = [
    df["math"].mean(),
    df["science"].mean(),
    df["english"].mean()
]
plt.figure(figsize=(7, 5))
bars = plt.bar(
    subjects,
    averages,
    color=["#3498db", "#2ecc71", "#e74c3c"],
    edgecolor="black"
)
for bar, avg in zip(bars, averages):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() - 3,
        f"{avg:.1f}",
        ha="center",
        va="top",
        color="white",
        fontweight="bold"
    )
plt.title("Average Scores by Subject")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("bar_chart.png", dpi=150)
plt.show()
plt.figure(figsize=(7, 5))

plt.hist(
    df["math"],
    bins=5,
    color="#9b59b6",
    edgecolor="black",
    alpha=0.8
)
plt.title("Distribution of Math Scores")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")

plt.axvline(
    df["math"].mean(),
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Mean: {df['math'].mean():.1f}"
)
plt.legend()
plt.tight_layout()
plt.savefig("histogram.png", dpi=150)
plt.show()
plt.figure(figsize=(8, 5))
plt.scatter(
    df["hours_studied"],
    df["math"],
    c=df["math"],
    cmap="viridis",
    s=100,
    edgecolors="black"
)

for i, name in enumerate(df["student"]):
    plt.annotate(
        name,
        (
            df["hours_studied"].iloc[i],
            df["math"].iloc[i]
        ),
        textcoords="offset points",
        xytext=(5, 5),
        fontsize=8
    )
plt.colorbar(label="Math Score")
plt.title("Hours Studied vs Math Score")
plt.xlabel("Hours Studied per Day")
plt.ylabel("Math Score")
plt.tight_layout()
plt.savefig("scatter.png", dpi=150)
plt.show()
numeric_df = df[
    ["math", "science", "english", "hours_studied"]
]

corr = numeric_df.corr()

plt.figure(figsize=(7, 5))

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    vmin=-1,
    vmax=1
)

plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig("heatmap.png", dpi=150)
plt.show()
melted=df.melt(id_vars="student",value_vars=["math","science","english"],var_name="subject",value_name="score")
plt.figure(figsize=(8,5))
sns.boxplot(x="subject",y="score",data=melted,palette=["#3498db","#2ecc71","#e74c3c"])
plt.tight_layout()
plt.savefig("boxplot.png",dpi=150)
plt.show()