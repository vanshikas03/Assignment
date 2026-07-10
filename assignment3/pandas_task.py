import pandas as pd

# Load CSV
df = pd.read_csv("student.csv")

# Filter score above 70
filtered = df[df["score"] > 70]

# Sort descending
filtered = filtered.sort_values(by="score", ascending=False)

# Print only name and score
print(filtered[["name", "score"]])