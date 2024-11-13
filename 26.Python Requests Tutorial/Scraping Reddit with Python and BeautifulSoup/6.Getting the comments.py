# find the Html tag
# with find()
# and convert into string
data_str = ""

for item in soup.find_all("p", class_="_1qeIAgB0cPwnLhDF9XSiJM"):
	data_str = data_str + item.get_text()
print(data_str)
