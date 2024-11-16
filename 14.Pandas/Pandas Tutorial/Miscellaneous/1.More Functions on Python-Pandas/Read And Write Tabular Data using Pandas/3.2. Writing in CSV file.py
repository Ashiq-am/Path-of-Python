# Reading the data from a CSV file named 'dataset.csv' into a pandas DataFrame
data = pd.read_csv('dataset.csv')

# Specifying the path for the new CSV file to be created
csv_file_path = 'newDataset.csv'

# Writing the DataFrame to a CSV file with the specified path, excluding the index column
data.to_csv(csv_file_path, index=False)

# Displaying a message indicating that the data has been successfully written to the CSV file
print(f'Data written to CSV file: {csv_file_path}')
