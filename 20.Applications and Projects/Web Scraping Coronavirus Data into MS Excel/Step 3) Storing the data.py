# List to store number of cases
data = []

# Find the span and get data from it
for i in cases:
	span = i.find('span')
	data.append(span.string)

# Dispaly number of cases
print(data)
