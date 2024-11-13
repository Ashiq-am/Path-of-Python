# Function to save multiple posts
def save_multiple(img_name,elem,last_img_flag = False):
	time.sleep(1)
	l = elem.get_attribute('innerHTML')
	html = bs(l,'html.parser')
	biglist = html.find_all('ul')
	biglist = biglist[0]
	list_images = biglist.find_all('li')
	if last_img_flag:
		user_image = list_images[-1]
	else:
		user_image = list_images[(len(list_images)//2)]
	video = user_image.find('video')
	if video:
		link = video['src']
	else:
		link = user_image.find('img')['src']
	response = requests.get(link)
	with open(img_name, 'wb') as f:
		f.write(response.content)
