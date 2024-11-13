from prettytable import PrettyTable


# open csv file
a = open("read_file.csv", 'r')

# read the csv file
a = a.readlines()

# Seperating the Headers
l1 = a[0]
l1 = l1.split(',')

# headers for table
t = PrettyTable([l1[0], l1[1]])

# Adding the data
for i in range(1, len(a)) :
	t.add_row(a[i].split(','))

code = t.get_html_string()
html_file = open('Tablee.html', 'w')
html_file = html_file.write(code)
