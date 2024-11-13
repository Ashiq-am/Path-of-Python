with open("sample.html", "r") as html_file:
	html = html_file.read()
	json_ = xmltojson.parse(html)
