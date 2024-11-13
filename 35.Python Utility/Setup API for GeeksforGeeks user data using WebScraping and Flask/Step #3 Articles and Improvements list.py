import requests
from bs4 import BeautifulSoup


def get_articles_and_improvements(user_handle):
	articles_and_improvements = {}

	url = "https://auth.geeksforgeeks.org/user/{}/articles".format(user_handle)

	response = requests.get(url)

	soup = BeautifulSoup(response.content, 'html5lib')

	contribute_section = soup.find('section', {'id': 'contribute'})
	improvement_section = soup.find('section', {'id': 'improvement'})

	contribution_list = contribute_section.find('ol')
	number_of_articles = 0
	articles = []
	if contribution_list:
		article_links = contribution_list.find_all('a')
		number_of_articles = len(article_links)
		for article in article_links:
			article_obj = {'title': article.text,
						'link': article['href']}
			articles.append(article_obj)

	articles_and_improvements['number_of_articles'] = number_of_articles
	articles_and_improvements['articles'] = articles

	improvement_list = improvement_section.find('ol')
	number_of_improvements = 0
	improvements = []
	if improvement_list:
		number_of_improvements = len(improvement_list)
		improvement_links = improvement_list.find_all('a')
		for improvement in improvement_links:
			improvement_obj = {'title': improvement.text,
							'link': improvement['href']}
			improvements.append(improvement_obj)

	articles_and_improvements['number_of_improvements'] = number_of_improvements
	articles_and_improvements['improvements'] = improvements

	return articles_and_improvements
