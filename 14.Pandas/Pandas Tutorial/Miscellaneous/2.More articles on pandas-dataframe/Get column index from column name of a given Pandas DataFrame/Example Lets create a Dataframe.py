# import pandas library
import pandas as pd

# dictionary
record = {'Math': [10, 20, 30,
				40, 70],
		'Science': [40, 50, 60,
					90, 50],
		'English': [70, 80, 66,
					75, 88]}

# create a dataframe
df = pd.DataFrame(record)

# show the dataframe
print(df)
