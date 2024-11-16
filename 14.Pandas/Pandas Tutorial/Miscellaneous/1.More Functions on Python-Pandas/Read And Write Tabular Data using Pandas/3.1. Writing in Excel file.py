# Reading the data from a CSV file named 'dataset.csv' into a pandas DataFrame
data = pd.read_csv('dataset.csv')

# Specifying the path for the new Excel file to be created
excel_file_path = 'newDataset.xlsx'

# Writing the DataFrame to an Excel file with the specified path, excluding the index column
data.to_excel(excel_file_path, index=False)

# Displaying a message indicating that the data has been successfully written to the Excel file
print(f'Data written to Excel file: {excel_file_path}')
