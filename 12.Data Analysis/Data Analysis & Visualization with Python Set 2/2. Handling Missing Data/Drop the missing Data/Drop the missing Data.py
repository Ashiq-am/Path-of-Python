import pandas as pd

# Create a DataFrame
dframe = pd.DataFrame({'Geeks': [23, 24, 22],
					'For': [10, 12, pd.np.nan],
					'geeks': [0, pd.np.nan, pd.np.nan]},
                      columns =['Geeks', 'For', 'geeks'])

# This will remove all the
# rows with NAN values

# If axis is not defined then
# it is along rows i.e. axis = 0
dframe.dropna(inplace = True)
print(dframe)

# if axis is equal to 1
dframe.dropna(axis = 1, inplace = True)

print(dframe)
