# importing the module
import pandas as pd

# creating the DataFrame
data = {"Number" : [0, 1, 2, 3, 4,
					5, 6, 7, 8, 9],
		"Alphabet" : ['A', 'B', 'C', 'D', 'E',
					'F', 'G', 'H', 'I', 'J']}
df = pd.DataFrame(data)

print("Initial max_rows value : " + str(pd.options.display.max_rows))

# displaying the DataFrame
display(df)

# changing the max_rows value
pd.set_option("display.max_rows", 5)

print("max_rows value after the change : " +
	str(pd.options.display.max_rows))

# displaying the DataFrame
display(df)
