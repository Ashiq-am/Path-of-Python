import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'John', 'Charlie'],
        'Age': [25, 30, 22, 35, 25, 28],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Salary': [50000, 55000, 40000, 70000, 50000, 48000]}

df = pd.DataFrame(data)
print(df)