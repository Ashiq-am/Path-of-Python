def start_requests(self):
	yield SeleniumRequest(
		url="https://www.geeksforgeeks.org/",
		wait_time=3,
		screenshot=True,
		callback=self.parse,
		dont_filter=True
	)
