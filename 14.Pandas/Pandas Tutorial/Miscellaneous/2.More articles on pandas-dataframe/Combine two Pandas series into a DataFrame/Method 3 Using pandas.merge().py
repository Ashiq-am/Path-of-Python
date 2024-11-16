# import pandas library
import pandas as pd

# create a series
a = pd.Series(["C++", "JAVA",
			"PYTHON", "DBMS",
			"C#"], name = "subjects")

# create a series
b = pd.Series(["30", "60",
			"90", "56",
			"50"], name = "marks")

# merge both series
df = pd.merge(a, b, right_index = True,
			left_index = True)
# show the dataframe
df
