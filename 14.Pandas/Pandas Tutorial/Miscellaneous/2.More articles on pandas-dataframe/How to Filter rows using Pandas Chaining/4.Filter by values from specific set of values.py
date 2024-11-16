# define the set of values
lst=['Uk','Australia']

# select the rows from specific set
# of values in a particular column
print(data[data.Country.isin(lst)])
