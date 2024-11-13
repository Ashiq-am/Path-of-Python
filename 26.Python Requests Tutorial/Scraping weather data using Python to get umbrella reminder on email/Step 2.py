city = "Hyderabad"
url = "https://www.google.com/search?q=" + "weather" + city
html = requests.get(url).content
