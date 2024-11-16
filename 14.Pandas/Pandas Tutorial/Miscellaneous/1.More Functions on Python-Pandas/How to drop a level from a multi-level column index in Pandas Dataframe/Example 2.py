# importing all important libraries
import pandas as pd

# Creating a multilevel index
index = pd.MultiIndex.from_tuples([("Company A", "Company B", "Company C"),
								("Company A", "Company A", "Company B"),
								("Company A", "Company B", "Company C")])

# Creating a pandas dataframe with
# multilevel-column indexing
df = pd.DataFrame([["Atreyi", "Digangana", "Sohom"],
				["Sujit", "Bjon", "Rajshekhar"],
				["Debosmita", "Shatabdi", ""]],
				columns=index)

# Labelling the dataframe index.
index = df. index
index. name = "ECE Placement"

# Showing the above multi-index column
# dataframe
print(df)
