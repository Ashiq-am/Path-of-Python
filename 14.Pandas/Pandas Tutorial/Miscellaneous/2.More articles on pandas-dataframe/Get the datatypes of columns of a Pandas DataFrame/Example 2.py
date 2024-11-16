# importing the module
import pandas as pd

# creating a DataFrame
data = {'Name' : ['Jai', 'Princi', 'Gaurav', 'Anuj'],
		'Age' : [27, 24, 22, 32],
		'Address' : ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
		'Qualification' : ['Msc', 'MA', 'MCA', 'Phd']}
table = pd.DataFrame(data)

print("Data Types of The Columns in Data Frame")
display(table.dtypes)
