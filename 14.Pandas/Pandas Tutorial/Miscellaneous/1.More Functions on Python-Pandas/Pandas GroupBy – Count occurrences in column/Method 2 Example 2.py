# import module
import pandas as pd


# assign data
data = pd.DataFrame({'Section': ['A', 'A', 'A', 'B', 'B', 'B',
								'C', 'C', 'C'],
					'Teacher': ['Kakeshi', 'Kakeshi', 'Iruka',
								'Kakeshi', 'Kakeshi', 'Kakeshi',
								'Iruka', 'Iruka', 'Guy']})

# display dataframe
print('Data:')
display(data)

print('Occurance counts of combined columns:')

# count occurances of combined columns
occur = data.groupby(['Section', 'Teacher']).size()

# diplay coccurances of combined columns
display(occur)
