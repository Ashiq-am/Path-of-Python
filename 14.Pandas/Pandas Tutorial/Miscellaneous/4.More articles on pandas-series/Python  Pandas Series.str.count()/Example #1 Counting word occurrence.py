# importing pandas package
import pandas as pd

# making list
list =["GeeksforGeeks", "Geeksforgeeks", "geeksforgeeks",
	"geeksforgeeks is a great platform", "for tech geeks"]

# making series
series = pd.Series(list)

# counting occurrence of geeks
count = series.str.count("geeks")

# display
count
