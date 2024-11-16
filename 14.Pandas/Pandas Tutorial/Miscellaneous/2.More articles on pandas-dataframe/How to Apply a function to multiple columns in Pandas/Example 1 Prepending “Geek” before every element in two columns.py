# imnport the module
import pandas as pd

# creating a DataFrame
df = pd.DataFrame({'String 1' :['Tom', 'Nick', 'Krish', 'Jack'],
				'String 2' :['Jane', 'John', 'Doe', 'Mohan']})

# displaying the DataFrame
display(df)

# function for prepending 'Geek'
def prepend_geek(name):
	return 'Geek ' + name

# executing the function
df[["String 1", "String 2"]] = df[["String 1", "String 2"]].apply(prepend_geek)

# displaying the DataFrame
display(df)
