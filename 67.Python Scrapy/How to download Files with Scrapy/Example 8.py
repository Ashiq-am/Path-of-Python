def parse_item(self, response):
	file_url = response.css('.downloadline::attr(href)').get()
	file_url = response.urljoin(file_url)
	file_extension = file_url.split('.')[-1]
	if file_extension not in ('zip', 'exe', 'msi'):
		return
	item = DownfilesItem()
	item['file_urls'] = [file_url]
	item['original_file_name'] = file_url.split('/')[-1]
	yield item
