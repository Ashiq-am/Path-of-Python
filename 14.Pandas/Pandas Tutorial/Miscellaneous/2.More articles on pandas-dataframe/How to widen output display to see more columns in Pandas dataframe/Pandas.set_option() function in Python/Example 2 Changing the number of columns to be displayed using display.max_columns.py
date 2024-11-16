# importing the module
import pandas as pd

# creating the DataFrame
data = {"Number" : 1,
		"Name" : ["ABC"],
		"Subject" : ["Computer"],
		"Field" : ["BDA"],
		"Marks" : 70}
df = pd.DataFrame(data)

print("Initial max_columns value : " +
	str(pd.options.display.max_columns))

# displaying the DataFrame
display(df)

# changing the max_columns value
pd.set_option("display.max_columns", 3)

print("max_columns value after the change : " +
	str(pd.options.display.max_columns))

# displaying the DataFrame
display(df)
