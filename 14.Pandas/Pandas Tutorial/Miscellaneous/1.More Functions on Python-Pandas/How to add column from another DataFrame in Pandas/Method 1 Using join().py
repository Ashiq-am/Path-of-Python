import pandas as pd


df1 = pd.DataFrame({"Col1": [1, 2, 3],
					"Col2": ["A", "B", "C"],
					"Col3": ["geeks", "for", "geeks"]})

print("First dataframe:")
display(df1)

df2 = pd.DataFrame({"C1": [4, 5, 6],
					"C2": ["D", "E", "F"]})

print("Second dataframe:")
display(df2)

extracted_col = df1["Col3"]
print("column to added from first dataframe to second:")
display(extracted_col)

df2 = df2.join(extracted_col)
print("Second dataframe after adding column from first dataframe:")
display(df2)
