import requests
from bs4 import BeautifulSoup

# input geeks for geeks article
article = 'extract-authors-information-from-geeksforgeeks-article-using-python'
index_Code = 3

# url
url = "https://www.geeksforgeeks.org/" + article


# Making a GET request
# to fetch article from
# geeksforgeeks servers
def getdata(url):
    r = requests.get(url)
    return r.text


def codescrapper(soup, article=None):
    codes_languages = soup.find_all('h2', class_='tabtitle')
    codes = soup.find_all("div", class_='code-container')
    count_codes_language = len(codes_languages)
    print(url)

    if article and article <= count_codes_language:
        print(codes[article - 1].get_text())

    else:
        for x in range(count_codes_language):
            print(codes[x].get_text())


if __name__ == '__main__':
    complete_article_html = getdata(url)
    soup = BeautifulSoup(complete_article_html, 'html.parser')
    codescrapper(soup, index_Code)
