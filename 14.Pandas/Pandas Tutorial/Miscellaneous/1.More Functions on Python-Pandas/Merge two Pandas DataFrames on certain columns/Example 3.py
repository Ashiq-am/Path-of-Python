# importing modules
import pandas as pd

# creating a dataframe
df1 = pd.DataFrame({'Name':['Raju', 'Rani', 'Geeta', 'Sita', 'Sohit'],
					'Marks':[80, 90, 75, 88, 59]})

# creating another dataframe with diffrent data
df2 = pd.DataFrame({'Name':['Raju', 'Divya', 'Geeta', 'Sita'],
					'Grade':['A', 'A', 'B', 'A'],
					'Rank':[3, 1, 4, 2 ],
					'Gender':['Male', 'Female', 'Female', 'Female']})
# display df1
display(df1)

# display df2
display(df2)

# applying merge with more parameters
df2.merge(df1[['Marks', 'Name']])
