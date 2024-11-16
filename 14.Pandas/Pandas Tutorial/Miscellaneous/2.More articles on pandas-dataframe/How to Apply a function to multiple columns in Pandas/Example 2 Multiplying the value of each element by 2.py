# imnport the module
import pandas as pd

# creating a DataFrame
df = pd.DataFrame({'Integers' :[1, 2, 3, 4, 5],
				'Float' :[1.1, 2.2, 3.3, 4.4 ,5.5]})

# displaying the DataFrame
display(df)

# function for prepending 'Geek'
def multiply_by_2(number):
	return 2 * number

# executing the function
df[["Integers", "Float"]] = df[["Integers", "Float"]].apply(multiply_by_2)

# displaying the DataFrame
display(df)
