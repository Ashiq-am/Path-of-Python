import pandas as pd

# reading csv files
data1 = pd.read_csv('datasets/loan.csv')
data2 = pd.read_csv('datasets/borrower.csv')

# using merge function by setting how='outer'
output4 = pd.merge(data1, data2,
				on='LOAN_NO',
				how='outer')

# displaying result
print(output4)
