import pandas as pd

# initialize list of lists
data = [['John', 8, 7, 6, 5], ['Paul', 8, 3, 6, 4],
		['Juli', 9, 10, 9, 9], ['Geeta', 9, 5, 4, 4]]

# Create the pandas DataFrame
df = pd.DataFrame(
	data, columns=['Name', 'Class', 'English',
				'Maths', 'History'])

# print dataframe.
print(df)
