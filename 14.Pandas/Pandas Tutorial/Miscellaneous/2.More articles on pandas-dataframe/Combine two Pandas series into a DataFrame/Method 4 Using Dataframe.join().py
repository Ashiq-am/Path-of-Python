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

# create a dataframe
a = pd.DataFrame(a)

# add series 'b'
# into dataframe 'a'
df = a.join(b)

# show the dataframe
df
