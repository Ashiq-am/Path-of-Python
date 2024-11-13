# extracting emails
def parse(self, response):
	EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
	emails = re.finditer(EMAIL_REGEX, str(response.text))
	for email in emails:
		self.email_list.append(email.group())

	for email in set(self.email_list):
		yield{
			"emails": email
		}

	self.email_list.clear()
