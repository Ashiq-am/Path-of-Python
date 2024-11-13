import pandas as pd

data = {
	"Shravan": {"Enrollment No.": 225, "Branch": "CSE", "CGPA": 7.5},
	"Jitu": {"Enrollment No.": 250, "Branch": "CSE", "CGPA": 7.0},
	"Ram": {"Enrollment No.": 249, "Branch": "CSE", "CGPA": 9.1},
}

print("DataFrame with columns as index and rows as values (orient='index')")
df_index = pd.DataFrame.from_dict(data, orient='index')
print(df_index)

print("\nDataFrame with values as columns and names as rows (orient='columns')")
df_columns = pd.DataFrame.from_dict(data, orient='columns')
print(df_columns)
