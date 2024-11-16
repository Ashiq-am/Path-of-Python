# Approach 2: Using recfromcsv function
import numpy as np
csv_data = """
ID,Name,Salary
1,Gaurav,50000
2,Yuvraj,60000
3,Pranav,55000
"""
with open('geeks_data.csv', 'w') as f:
    f.write(csv_data)
data = np.recfromcsv('geeks_data.csv', encoding=None)
print("Record array:")
print(data)
