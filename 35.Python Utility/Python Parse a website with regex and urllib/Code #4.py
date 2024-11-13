paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for eachP in paragraphs:
	print(eachP)
