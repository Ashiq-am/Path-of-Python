import csv

# Step 1: Read the existing CSV file and store its content
csv_file_path = 'mon.csv'
with open(csv_file_path, 'r') as file:
	reader = csv.reader(file)
	data = list(reader)

# Step 2: Define the values for the new "City" column
new_city_values = ['New York', 'Los Angeles', 'Chicago', 'San Francisco']

# Step 3: Add the new "City" column header to the first row of the data
data[0].append('City')

# Step 4: Add the new "City" column values to the remaining rows of the data
for i in range(1, len(data)):
	data[i].append(new_city_values[i - 1])

# Step 5: Write the updated data back to the CSV file
with open(csv_file_path, 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerows(data)
