def make_tiny(url):
	request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
	with contextlib.closing(urlopen(request_url)) as response:
		return response.read().decode('utf-8 ')
