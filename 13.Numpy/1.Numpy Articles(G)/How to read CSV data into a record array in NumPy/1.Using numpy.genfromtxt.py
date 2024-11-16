# Approach 1: Using numpy.genfromtxt

import numpy as np

csv_data = """
ID,Name,Salary
1,Gaurav,50000
2,Yuvraj,60000
3,Pranav,55000
"""
with open('geeks_data.csv', 'w') as f:
    f.write(csv_data)

data = np.genfromtxt('geeks_data.csv', delimiter=',',
                     dtype=None, names=True, encoding=None)

print("Record array:")
print(data)
