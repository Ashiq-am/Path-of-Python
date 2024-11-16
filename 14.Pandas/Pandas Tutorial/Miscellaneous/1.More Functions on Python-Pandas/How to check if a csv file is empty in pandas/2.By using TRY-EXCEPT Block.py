import pandas as pd

csv_file_path = '/content/data_2.csv'

try:
	df = pd.read_csv(csv_file_path) #read the CSV file

	if df.empty: # Check if the DataFrame is empty
		print('CSV file is empty')
	else:
		# Proceed with data processing
		print(df.head())
except pd.errors.EmptyDataError:
	print('CSV file is empty')
except FileNotFoundError:
	print('CSV file not found')
