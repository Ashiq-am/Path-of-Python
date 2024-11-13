import csv

# Step 1: Read the CSV File
with open('numbers.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Step 2: Perform Addition Operation
for row in data:
    try:
        a = int(row[0])
        b = int(row[1])
        row.append(a + b)
    except ValueError:
        row.append('')

# Step 3: Write Back to CSV File
with open('numbers_updated.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Addition completed and updated CSV file created successfully.")
