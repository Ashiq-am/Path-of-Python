import csv

# Function to compare two CSV files
def compare(file1, file2):
    differences = []

    # Open both CSV files in read mode
    with open(file1, 'r') as csv_file1, open(file2, 'r') as csv_file2:
        reader1 = csv.reader(csv_file1)
        reader2 = csv.reader(csv_file2)

        # Iterate over rows in both files simultaneously
        for row1, row2 in zip(reader1, reader2):
            if row1 != row2:
                differences.append((row1, row2))

    return differences

# Define file paths
file1 = 'file1.csv'
file2 = 'file2.csv'

# Call the compare_csv_files function and store the differences
differences = compare(file1, file2)
for diff in differences:
    print(f"Difference found: {diff}")
