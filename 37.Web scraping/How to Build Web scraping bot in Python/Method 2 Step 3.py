# since, headings are the first row of the table
headings = data.find_all('tr')[0]
headings_list = [] # list to store all headings

for x in headings:
	headings_list.append(x.text)
# since, we require only the first ten columns
headings_list = headings_list[:10]

print('Headings are: ')
for column in headings_list:
	print(column)
