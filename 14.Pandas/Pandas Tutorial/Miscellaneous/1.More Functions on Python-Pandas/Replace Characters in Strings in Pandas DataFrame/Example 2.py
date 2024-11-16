# import pandas
import pandas as pd

data = {'first': ['abcp', 'xyzp', 'mpok',
				'qrps', 'ptuw'],
		'second': ['abcp', 'xyzp', 'mpok',
				'qrps', 'ptuw']
		}
# create an dataframe
df = pd.DataFrame(data, columns=['first', 'second'])

# print dataframe
print("\n original dataframe \n\n", df)

# replace '_' with '='
df['first'] = df['first'].str.replace('p', '-')

# print dataframe
print("\n\n After replace character \n\n", df)
