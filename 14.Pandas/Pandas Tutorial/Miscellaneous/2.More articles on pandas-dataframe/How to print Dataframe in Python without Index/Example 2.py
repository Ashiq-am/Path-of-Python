import pandas as pd

df = pd.DataFrame(["Geeks", "for", "geek"],

				index=["A", "B", "C"])

print("THIS IS THE ORIGINAL DATAFRAME:")
dislay(df)
print()

print("THIS IS THE DATAFRMAE WITHOUT INDEX VAL")
print(df.to_string(index=False))
