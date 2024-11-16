import pandas as pd

# reading csv files
data1 = pd.read_csv('datasets/loan.csv')
data2 = pd.read_csv('datasets/borrower.csv')

# using merge function by setting how='right'
output3 = pd.merge(data1, data2,
				on='LOAN_NO',
				how='right')

# displaying result
print(output3)
