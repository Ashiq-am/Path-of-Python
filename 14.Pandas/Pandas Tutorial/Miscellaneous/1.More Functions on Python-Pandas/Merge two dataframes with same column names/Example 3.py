# import module
import pandas as pd

# assign dataframes
data1 = pd.DataFrame([[25, 77.5, 'A'], [30, 60.2, 'B'],
					[25, 70.7, 'C']],
					columns=['Students', 'Avg Marks', 'Section'])

data2 = pd.DataFrame([[30, 70.2, 'A'], [25, 65.2, 'B'],
					[35, 77.7, 'C']],
					columns=['Students', 'Avg Marks', 'Section'])


# display dataframes
print('Dataframes:')
display(data1)
display(data2)

# merge two data frames
print('After merging:')
pd.concat([data1, data2], axis=0)
