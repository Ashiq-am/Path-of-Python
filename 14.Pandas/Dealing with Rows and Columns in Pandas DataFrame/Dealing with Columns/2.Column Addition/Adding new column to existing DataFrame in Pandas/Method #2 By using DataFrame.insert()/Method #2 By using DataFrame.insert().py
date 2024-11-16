''''''
'''It gives the freedom to add a column at any position we like and not just at the end. It also provides 
different options for inserting the column values.'''



# Import pandas package
import pandas as pd

# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
		'Height': [5.1, 6.2, 5.1, 5.2],
		'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Using DataFrame.insert() to add a column
df.insert(2, "Age", [21, 23, 24, 21], True)

# Observe the result
df
