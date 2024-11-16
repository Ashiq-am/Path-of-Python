import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Initialize an empty list to store the results
results = []

# Iterate over each row
for i in range(len(df)):
    row_results = []
    for j in range(len(df)):
        if i != j:
            # Compare rows and append the result
            comparison = df.iloc[i] == df.iloc[j]
            row_results.append(comparison.all())
        else:
            row_results.append(False)
    results.append(row_results)

print("\nResults (Iterative Comparison):\n", results)
