# Python program to generate a heatmap
# which represents the correlation between
# columns of panda dataframe

# import required libraries
import pandas as pd
import seaborn as sn

# Defining figure size
# for the output plot
fig, ax = plt.subplots(figsize = (12, 7))

# Defining index for the dataframe
idx = ['1', '2', '3', '4']

# Defining columns for the dataframe
cols = list('ABCD')

# Entering values in the index and columns
# and converting them into a panda dataframe
df = pd.DataFrame([[10, 20, 30, 40], [50, 30, 8, 15],
				[25, 14, 41, 8], [7, 14, 21, 28]],
				columns = cols, index = idx)

df = pd.DataFrame(df, columns =['A', 'B', 'C', 'D'])

corr = df.corr()
sn.heatmap(corr, annot = True)
