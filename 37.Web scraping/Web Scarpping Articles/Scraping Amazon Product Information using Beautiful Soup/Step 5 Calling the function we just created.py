if __name__ == '__main__':
# openning our url file to access URLs
	file = open("url.txt", "r")

	# iterating over the urls
	for links in file.readlines():
		main(links)
