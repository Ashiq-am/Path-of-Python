def rev_img(soup):

	# find the Html tag
	# with find()
	# and convert into string
	data_str = ""
	cus_list = []
	images = []
	for img in soup.findAll('img', class_="cr-lightbox-image-thumbnail"):
		images.append(img.get('src'))
	return images


img_result = rev_img(soup)
img_result
