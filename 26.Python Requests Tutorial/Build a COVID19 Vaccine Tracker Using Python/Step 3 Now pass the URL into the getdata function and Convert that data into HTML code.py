from bs4 import BeautifulSoup
from numpy.ma import getdata

htmldata = getdata("https://covid-19tracker.milkeninstitute.org/")
soup = BeautifulSoup(htmldata, 'html.parser')
res = soup.find_all("div", class_="is_h5-2 is_developer w-richtext")
print(str(res))
