# importing libraries
from bs4 import BeautifulSoup as BS
import requests


# method to get the info
def get_info(country_name):
    # creating url using country name
    url = "https://www.worldometers.info/coronavirus/country/" + country_name + "/"

    # getting the request from url
    data = requests.get(url)

    # converting the text
    soup = BS(data.text, 'html.parser')

    # finding meta info for cases
    cases = soup.find_all("div", class_="maincounter-number")

    # getting total cases number
    total = cases[0].text

    # filtering it
    total = total[1: len(total) - 2]

    # getting recovered cases number
    recovered = cases[2].text

    # filtering it
    recovered = recovered[1: len(recovered) - 1]

    # getting death cases number
    deaths = cases[1].text

    # filtering it
    deaths = deaths[1: len(deaths) - 1]

    # saving details in dictionary
    ans = {'Total Cases': total, 'Recovered Cases': recovered,
           'Total Deaths': deaths}

    # returnng the dictionary
    return ans


# setting country name
country_name = "us"

# calling the get_info method
us = get_info(country_name)

# printing the results for us
print("Cases in United States")
for i, j in us.items():
    print(i + " : " + j)

print("----------------------------")
# setting country name to india
country_name = "india"

# calling the get_info method
india = get_info(country_name)

# printing the results for us
print("Cases in India")
for i, j in india.items():
    print(i + " : " + j)
