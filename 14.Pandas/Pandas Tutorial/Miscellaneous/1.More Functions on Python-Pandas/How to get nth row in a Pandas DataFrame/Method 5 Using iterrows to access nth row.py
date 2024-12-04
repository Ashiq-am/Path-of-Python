import pandas as pd

# Create a DataFrame with new data
data = {
    'Employee': ['John', 'Emma', 'Liam', 'Sophia', 'Olivia'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales'],
    'Salary': [50000, 60000, 70000, 55000, 45000]
}

df = pd.DataFrame(data)

# Access the 3rd row using iterrows()
for index, row in df.iterrows():
    if index == 2:
        nth_row = row
        break

print(nth_row)