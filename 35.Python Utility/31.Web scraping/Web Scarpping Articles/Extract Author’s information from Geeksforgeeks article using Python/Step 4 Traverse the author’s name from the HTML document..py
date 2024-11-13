# traverse auther name
for i in soup.find('div', class_="author_handle"):
	Author = i.get_text()
print(Author)
