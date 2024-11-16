import pandas as pd
arr = pd.array([1, 2, None], dtype="Int64")

df = pd.DataFrame({"Numbers": pd.array([10, None, 20], dtype="Int64")})

print(df)
