# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# setting first name as index column
data.set_index(["First Name", "Gender"], inplace = True,
							append = True, drop = True)

# resetting index
data.reset_index(level = 2, inplace = True, col_level = 1)

# display
data.head()
