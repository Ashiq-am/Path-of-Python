import requests
from bs4 import BeautifulSoup


def get_profile_detail(user_handle):

	url = "https://auth.geeksforgeeks.org/user/{}/profile".format(user_handle)

	response = requests.get(url)

	soup = BeautifulSoup(response.content, 'html5lib')

	description_div = soup.find('div', {'class': 'descDiv'})

	if not description_div:
		return None

	user_details_div = description_div.find('div', {'class': 'mdl-cell'})

	specific_details = user_details_div.find_all('div', {'class': 'mdl-grid'})

	user_profile = {}

	for detail_div in specific_details:

		block = detail_div.find_all('div', {'class': 'mdl-cell'})

		attribute = block[0].text.strip()
		value = block[1].text.strip()

		user_profile[attribute] = value

	return {'user profile': user_profile}
