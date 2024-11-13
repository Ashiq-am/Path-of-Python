import re # for removing the extra blank spaces

location_html = soup.find_all(
	'ul', {'class': 'job-card-container__metadata-wrapper'})

location_list = []

for loc in location_html:
	res = re.sub('\n\n +', ' ', loc.text.strip())

	location_list.append(res)

print(location_list)
