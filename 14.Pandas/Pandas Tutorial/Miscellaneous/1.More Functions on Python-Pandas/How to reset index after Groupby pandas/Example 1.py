# import required modules
import numpy as np
import pandas as pd

# creating dataframe
df = pd.DataFrame({'Subject': ['Physics',
							'Chemistry',
							'Maths'],
				'Marks': [4, 8, 5]})

# grouping the data on the basis of
# subject and mean of marks.
df_grouped = df.groupby(['Subject']).mean()

# display dataset
df_grouped
