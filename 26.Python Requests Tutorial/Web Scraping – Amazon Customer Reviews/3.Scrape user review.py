def cus_rev(soup):
	# find the Html tag
	# with find()
	# and convert into string
	data_str = ""

	for item in soup.find_all("div", class_="a-expander-content \
	reviewText review-text-content a-expander-partial-collapse-content"):
		data_str = data_str + item.get_text()

	result = data_str.split("\n")
	return (result)


rev_data = cus_rev(soup)
rev_result = []
for i in rev_data:
	if i is "":
		pass
	else:
		rev_result.append(i)
rev_result
