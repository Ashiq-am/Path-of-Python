# importing libraries
from bs4 import BeautifulSoup as BS
import requests


# method to get the info
def get_info(url):
    # getting the request from url
    data = requests.get(url)

    # converting the text
    soup = BS(data.text, 'html.parser')

    # finding meta info for total cases
    total = soup.find("div", class_="maincounter-number").text

    # filtering it
    total = total[1: len(total) - 2]

    # finding meta info for other numbers
    other = soup.find_all("span", class_="number-table")

    # getting recovered cases number
    recovered = other[2].text

    # getting death cases number
    deaths = other[3].text

    # filtering the data
    deaths = deaths[1:]

    # saving details in dictionary
    ans = {'Total Cases': total, 'Recovered Cases': recovered,
           'Total Deaths': deaths}

    # returnng the dictionary
    return ans


# url of the corona virus cases
url = "https://www.worldometers.info/coronavirus/"

# calling the get_info method
ans = get_info(url)

# printing the ans
for i, j in ans.items():
    print(i + " : " + j)
