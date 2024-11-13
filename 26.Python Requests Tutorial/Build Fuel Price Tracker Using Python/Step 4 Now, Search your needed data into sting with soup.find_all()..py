# Declare string var
# Declare list
mydatastr = ''
result = []

# searching all tr in the html data
# storing as a string
for table in soup.find_all('tr'):
	mydatastr += table.get_text()

# set accourding to your required
mydatastr = mydatastr[1:]
itemlist = mydatastr.split("\n\n")

for item in itemlist[:-5]:
	result.append(item.split("\n"))

result
