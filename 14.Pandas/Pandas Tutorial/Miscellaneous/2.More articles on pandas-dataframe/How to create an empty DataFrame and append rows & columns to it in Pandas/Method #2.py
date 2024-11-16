# import pandas library as pd
import pandas as pd

# create an Empty DataFrame
# object With column names only
df = pd.DataFrame(columns = ['Name', 'Articles', 'Improved'])
print(df)

# append rows to an empty DataFrame
df = df.append({'Name' : 'Ankit', 'Articles' : 97, 'Improved' : 2200},
				ignore_index = True)
df = df.append({'Name' : 'Aishwary', 'Articles' : 30, 'Improved' : 50},
				ignore_index = True)
df = df.append({'Name' : 'yash', 'Articles' : 17, 'Improved' : 220},
			ignore_index = True)

df
