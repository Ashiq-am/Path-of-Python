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

print('Occurance counts of particular columns:')

# count occurances a particular column
occur = data.groupby(['Section']).size()

# diplay coccurances of a particular column
display(occur)

# count occurances a particular column
occur = data.groupby(['Teacher']).size()

# diplay coccurances of a particular column
display(occur)
