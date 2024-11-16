# importing pandas library
import pandas as pd

# creating and initializing a list
values = [['Rohan', 455], ['Elvish', 250], ['Deepak', 495],
		['Sai', 400], ['Radha', 350], ['Vansh', 450]]

# creating a pandas dataframe
df = pd.DataFrame(values, columns=['Name', 'Univ_Marks'])

# Applying lambda function to find percentage of
# 'Univ_Marks' column using df.assign()
df = df.assign(Percentage=lambda x: (x['Univ_Marks'] / 500 * 100))

# displaying the data frame
df
