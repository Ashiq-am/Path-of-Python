# Approach 3: Using pandas and converting to NumPy record array

import numpy as np
import pandas as pd
csv_data = """
ID,Name,Salary
1,Gaurav,50000
2,Yuvraj,60000
3,Pranav,55000
"""
with open('geeks_data.csv', 'w') as f:
    f.write(csv_data)
df = pd.read_csv('geeks_data.csv')
data = df.to_records(index=False)
print("Record array:")
print(data)
