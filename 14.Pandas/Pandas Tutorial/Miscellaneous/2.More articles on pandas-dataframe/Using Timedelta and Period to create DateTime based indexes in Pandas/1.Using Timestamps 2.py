# importing pandas as pd
import pandas as pd

# Let's create a dataframe
df = pd.DataFrame({'City':['Lisbon', 'Parague', 'Macao', 'Venice'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
					'Cost':[10000, 5000, 15000, 2000]})


# Let's create an index using Timestamps
index_ = [pd.Timestamp('01-06-2018'), pd.Timestamp('04-06-2018'),
		pd.Timestamp('07-06-2018'), pd.Timestamp('10-06-2018')]

# Let's set the index of the dataframe
df.index = index_

# Let's visualize the dataframe
print(df)
