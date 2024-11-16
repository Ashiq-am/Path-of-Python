# import python pandas package
import pandas as pd

# import the numpy package
import numpy as np

# Create sample dataframe data1 and data2
data1 = pd.DataFrame(np.random.randint(100, size=(1000, 3)),
					columns=['EMI', 'Salary', 'Debt'])
data2 = pd.DataFrame(np.random.randint(100, size=(1000, 3)),
					columns=['Salary', 'Debt', 'Bonus'])

# Merge the DataFrames
merged = pd.merge(data1, data2, how='inner',
				left_on=['Salary', 'Debt'],
				right_on=['Salary', 'Debt'])

print(merged)
