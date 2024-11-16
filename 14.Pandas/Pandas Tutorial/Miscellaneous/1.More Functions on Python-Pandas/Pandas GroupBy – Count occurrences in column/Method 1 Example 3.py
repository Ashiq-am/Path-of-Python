# import module
import pandas as pd


# assign data
data = pd.read_csv('diamonds.csv')

# display dataframe
print('Data:')
display(data.sample(10))

print('Occurance counts of particular column:')

# count occurances a particular column
occur = data.groupby(['cut']).size()

# diplay coccurances of a particular column
display(occur)

print('Occurance counts of combined columns:')

# count occurances of combined columns
occur = data.groupby(['clarity', 'color', 'cut']).size()

# diplay coccurances of combined columns
display(occur)
