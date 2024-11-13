web_page_paragraph_contents = soup('p')
web_page_data = ''
for para in web_page_paragraph_contents:
	web_page_data = web_page_data + str(para.text)
