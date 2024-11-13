def product_info(soup):

	# find the Html tag
	# with find()
	# and convert into string
	data_str = ""
	pro_info = []

	for item in soup.find_all("ul", class_="a-unordered-list a-nostyle\
	a-vertical a-spacing-none detail-bullet-list"):
		data_str = data_str + item.get_text()
		pro_info.append(data_str.split("\n"))
		data_str = ""
	return pro_info


pro_result = product_info(soup)

# Filter the required data
for item in pro_result:
	for j in item:
		if j is "":
			pass
		else:
			print(j)
