# Python program to generate heatmap
# which represents correlation between
# columns of panda dataframe

# import required libraries
import pandas as pd

# Defining index for the dataframe
idx = ['1', '2', '3', '4']

# Defining columns for the dataframe
cols = list('ABCD')

# Entering values in the index and columns
# and converting them into a panda dataframe
df = pd.DataFrame([[10, 20, 30, 40], [50, 30, 8, 15],
				[25, 14, 41, 8], [7, 14, 21, 28]],
				columns = cols, index = idx)

# generating pairwise correlation
corr = df.corr()

# Displaying dataframe as an heatmap
# with diverging colourmap as coolwarm
corr.style.background_gradient(cmap ='coolwarm')
