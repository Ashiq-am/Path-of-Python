# sending requests
	def start_requests(self):
		for results in search(self.query, num=10, stop=None, pause=2):
			yield SeleniumRequest(
				url=results,
				callback=self.parse,
				wait_until=EC.presence_of_element_located(
					(By.TAG_NAME, "html")),
				dont_filter=True
			)
