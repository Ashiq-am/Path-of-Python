import numpy as np
import csv

# Read the CSV file (replace 'data.csv' with your file path)
with open('data.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader) # Skip the header row
	data = np.array(list(reader), dtype=int)

# Calculate column averages
age_avg = np.mean(data[:, 0]) # Column 0 (Age)
salary_avg = np.mean(data[:, 1]) # Column 1 (Salary)

# Display the results
print(f"Average Age: {age_avg:.2f}")
print(f"Average Salary: ${salary_avg:.2f}")
