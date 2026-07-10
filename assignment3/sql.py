import pandas as pd

# Load CSV
df = pd.read_csv("students.csv")

# Filter and sort
result = (
    df[df["score"] > 70]
    .sort_values(by="score", ascending=False)
)

# Print name and score
print(result[["name", "score"]])