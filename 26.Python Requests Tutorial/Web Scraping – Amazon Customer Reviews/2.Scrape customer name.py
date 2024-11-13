def cus_data(soup):
	# find the Html tag
	# with find()
	# and convert into string
	data_str = ""
	cus_list = []

	for item in soup.find_all("span", class_="a-profile-name"):
		data_str = data_str + item.get_text()
		cus_list.append(data_str)
		data_str = ""
	return cus_list


cus_res = cus_data(soup)
print(cus_res)
