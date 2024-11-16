# import module
import pandas as pd

# assign dataframes
data1 = pd.DataFrame([[25, 77.5, 'A'], [30, 60.2, 'B']],
					columns=['Students', 'Avg Marks', 'Section'])

data2 = pd.DataFrame([[52, 'C'], [25, 'A']],
					columns=['Students', 'Section'])

# display dataframes
print('Dataframes:')
display(data1)
display(data2)

# merge two data frames
print('After merging:')
pd.concat([data1, data2], axis=0)
