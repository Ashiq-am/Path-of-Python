# importing necessary libraries
import requests
from bs4 import BeautifulSoup


# creating a function in which we will accept the url and
# fetch the html content from the url using request and apply the parser function on it
def strongText(url):
    r = requests.get(url)

    TextData = BeautifulSoup(r.content, 'html.parser')

    st = TextData.find_all('strong')

    # displaying the data
    for data in st:
        print(data.text)


if __name__ == "__main__":
    # input url
    url = 'https://www.geeksforgeeks.org/machine-learning-types-of-artificial-intelligence/'

    # function calling
    strongText(url)
