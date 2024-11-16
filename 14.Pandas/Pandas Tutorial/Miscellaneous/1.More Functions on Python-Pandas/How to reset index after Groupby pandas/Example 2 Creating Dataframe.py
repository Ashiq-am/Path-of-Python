# import required modules
import pandas as pd
import numpy as np

# creating dataframe
df2 = pd.DataFrame({'Student': [1, 2, 3, 4, 1, 3, 2, 4, 1, 2, 4, 3],
					'Amount': [
				10, 20, 30, 40, 20, 60, 40, 80, 30, 60, 120, 90]})

# grouping the data
df2_group = df2.groupby(['Student'])

# grouped on the basis of students and
# with the value of count of amount
df2_grouped = df2_group['Amount'].value_counts()

# display dataset
print(df2_grouped)
