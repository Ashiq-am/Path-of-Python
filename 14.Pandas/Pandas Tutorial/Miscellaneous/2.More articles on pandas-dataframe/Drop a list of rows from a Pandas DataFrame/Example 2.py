# creating a DataFrame
data = {'Name' : ['Jai', 'Princi', 'Gaurav', 'Anuj'],
		'Age' : [27, 24, 22, 32],
		'Address' : ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
		'Qualification' : ['Msc', 'MA', 'MCA', 'Phd']}
table = pd.DataFrame(data)

# original DataFrame
display("Original DataFrame")
display(table)

# drop 2nd row
display("Dropped 2nd row")
display(table.drop(1))
