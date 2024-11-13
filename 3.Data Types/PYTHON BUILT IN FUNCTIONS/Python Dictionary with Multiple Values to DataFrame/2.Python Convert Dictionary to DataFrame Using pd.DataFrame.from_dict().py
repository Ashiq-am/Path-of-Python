import pandas as pd
data = {
	"Shravan": {"Enrollment No.": 225, "Branch": "CSE", "CGPA": 7.5},
	"Jitu": {"Enrollment No.": 250, "Branch": "CSE", "CGPA": 7.0},
	"Ram": {"Enrollment No.": 249, "Branch": "CSE", "CGPA": 9.1},
}

df = pd.DataFrame.from_dict(data)
print(df)
