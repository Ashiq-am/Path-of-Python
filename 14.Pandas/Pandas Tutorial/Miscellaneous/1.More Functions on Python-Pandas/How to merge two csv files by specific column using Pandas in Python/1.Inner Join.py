import pandas as pd

# reading two csv files
data1 = pd.read_csv('datasets/loan.csv')
data2 = pd.read_csv('datasets/borrower.csv')

# using merge function by setting how='inner'
output1 = pd.merge(data1, data2,
				on='LOAN_NO',
				how='inner')

# displaying result
print(output1)
