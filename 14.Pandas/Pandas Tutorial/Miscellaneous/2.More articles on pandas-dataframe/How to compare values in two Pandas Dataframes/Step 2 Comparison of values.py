# add the Price2 column from
# df2 to df1
df1['Price_2'] = df2['Price_2']

# create new column in df1 to
# check if prices match
df1['Price_Matching'] = np.where(df1['Price_1'] == df2['Price_2'],
								'True', 'False')
df1
