# path of the chromedriver we have just downloaded
PATH = r"D:\chromedriver"
driver = webdriver.Chrome(PATH) # to open the browser

# url of google news website
url = 'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en'

# to open the url in the browser
driver.get(url)
