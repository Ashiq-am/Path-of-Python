import pandas as pd

df = pd.DataFrame([["1", "2"], ["3", "4"]],
				columns = ["a", "b"])

df["a"] = df["a"].astype(str).astype(int)

print(df.dtypes)
