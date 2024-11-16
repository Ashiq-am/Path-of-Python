import pandas as pd

# Specify the path to CSV file
csv_file_path = '/content/data_2.csv'

df = pd.read_csv(csv_file_path) # read csv file

if df.empty: # check if file is empty
	print('File is empty')
else:
	# proceed with reading the file
	print(df.head())
