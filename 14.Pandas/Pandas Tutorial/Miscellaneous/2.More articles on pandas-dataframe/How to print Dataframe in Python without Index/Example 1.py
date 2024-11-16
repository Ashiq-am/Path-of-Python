import pandas as pd

df = pd.DataFrame({"Name": ["sachin", "sujay", "Amara", "shivam",
							"Manoj"],

				"Stream": ["Humanities", "Science", "Science",
							"Commerce", "Humanities"]},

				index=["A", "B", "C", "D", "E"])

print("THIS IS THE ORIGINAL DATAFRAME:")
display(df)
print()

print("THIS IS THE DATAFRMAE WITHOUT INDEX VAL")
print(df.to_string(index=False))
