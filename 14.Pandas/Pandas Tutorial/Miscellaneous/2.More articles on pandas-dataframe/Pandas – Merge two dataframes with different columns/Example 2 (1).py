# initialize list of lists
data1 = [['Haseen', 88.00, 5], ['ramya', 54.00, 5], ['haritha', 56.34, 4]]

# Create the pandas DataFrame
df1 = pd.DataFrame(
	data1, columns=['Name', 'Marks', 'Total subjects registered'])

# print dataframe.
df1
