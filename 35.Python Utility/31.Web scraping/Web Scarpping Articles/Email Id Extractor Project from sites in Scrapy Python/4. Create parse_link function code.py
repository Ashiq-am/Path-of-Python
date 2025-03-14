def parse_link(self, response):
	# response.meta['links'] this helps to get links list
	links = response.meta['links']
	flag = 0

	# links that contains following bad words are discarded
	bad_words = ['facebook', 'instagram', 'youtube', 'twitter', 'wiki', 'linkedin']

	for word in bad_words:
		# if any bad word is found in the current page url
		# flag is assigned to 1
		if word in str(response.url):
			flag = 1
			break

	# if flag is 1 then no need to get email from
	# that url/page
	if (flag != 1):
		html_text = str(response.text)
		# regular expression used for email id
		email_list = re.findall('\w+@\w+\.{1}\w+', html_text)
		# set of email_list to get unique
		email_list = set(email_list)
		if (len(email_list) != 0):
			for i in email_list:
				# adding email ids to final uniqueemail
				self.uniqueemail.add(i)

	# parse_link function is called till
	# if condition satisfy
	# else move to parsed function
	if (len(links) > 0):
		l = links[0]
		links.pop(0)
		yield SeleniumRequest(
			url=l,
			callback=self.parse_link,
			dont_filter=True,
			meta={'links': links}
		)
	else:
		yield SeleniumRequest(
			url=response.url,
			callback=self.parsed,
			dont_filter=True
		)
