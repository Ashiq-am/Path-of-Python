# import required modules
import numpy as np
import pandas as pd

# creating dataframe
df = pd.DataFrame({'Subject': ['B',
							'C',
							'A','D','C','B','A'],
				'Marks': [4, 8, 5,9,8,1,0]})

# grouping the data on the basis of
# subject and mean of marks.
df_grouped = df.groupby(['Subject']).mean()

# display dataset
df_grouped

# reset index
df_grouped.reset_index()
