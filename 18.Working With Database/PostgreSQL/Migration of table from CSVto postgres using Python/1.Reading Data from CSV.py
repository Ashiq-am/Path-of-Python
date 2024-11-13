import pandas

file = 'data.csv'
data = pandas.read_csv(file)
print(data.head())
