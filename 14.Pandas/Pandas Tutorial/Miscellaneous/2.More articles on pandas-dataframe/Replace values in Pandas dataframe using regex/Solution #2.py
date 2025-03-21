# importing pandas as pd
import pandas as pd

# Let's create a Dataframe
df = pd.DataFrame({'City':['New York (City)', 'Parague', 'New Delhi (Delhi)', 'Venice', 'new Orleans'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
					'Cost':[10000, 5000, 15000, 2000, 12000]})


# Let's create the index
index_ = [pd.Period('02-2018'), pd.Period('04-2018'),
		pd.Period('06-2018'), pd.Period('10-2018'), pd.Period('12-2018')]

# Set the index
df.index = index_

# Let's print the dataframe
print(df)
