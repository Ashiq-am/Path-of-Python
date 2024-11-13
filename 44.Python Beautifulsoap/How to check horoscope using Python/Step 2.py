# importing necessary modules
import requests
from bs4 import BeautifulSoup


def horoscope(zodiac_sign: int, day: str) -> str:
    # website taking the user input variables
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )

    # soup will contain all the website's data
    soup = BeautifulSoup(requests.get(url).content,
                         "html.parser")
    # print(soup)

    # we will search for main-horoscope
    # class and we will simply return it
    return soup.find("div", class_="main-horoscope").p.text
