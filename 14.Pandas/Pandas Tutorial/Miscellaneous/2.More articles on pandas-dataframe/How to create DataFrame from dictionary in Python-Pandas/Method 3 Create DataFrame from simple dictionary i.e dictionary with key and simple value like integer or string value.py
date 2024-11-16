# import pandas library
import pandas as pd

# dictionary
details = {
	'Ankit' : 22,
	'Golu' : 21,
	'hacker' : 23
	}

# creating a Dataframe object from a list
# of tuples of key, value pair
df = pd.DataFrame(list(details.items()))

df
