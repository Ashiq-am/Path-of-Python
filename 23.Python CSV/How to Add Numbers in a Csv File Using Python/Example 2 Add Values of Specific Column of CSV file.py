import csv
from decimal import Decimal, InvalidOperation

# Reads the CSV file and returns the data as a list of rows.
def read_csv_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Iterates over the data and calculates the sum of numbers in a specific column.
def sum_numbers(data, column_index):
    total = Decimal(0)
    for row in data:
        try:
            number = Decimal(row[column_index])
            total += number
        except (ValueError, InvalidOperation):
            print(f"Invalid value in row: {row}")
    return total

# Writes the total to a new CSV file.
def write_total_to_csv(total, output_file):
    with open(output_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Total'])
        csv_writer.writerow([total])
        print(f"Total: {total}")

# Displays the total on the console.
def display_total(total):
    print(f"Total: {total}")

# Driver's code
data = read_csv_file('input.csv')

# Adjust the column index according to CSV file
total = sum_numbers(data, column_index=2)

# Output the total to a new CSV file
write_total_to_csv(total, 'output.csv')
