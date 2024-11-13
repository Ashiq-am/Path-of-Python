from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def pageLoad(url):
    options = Options()

    # we initially set the page load stategy to normal
    # which means it wait for the complete web pages to load.
    options.page_load_strategy = 'normal'
    dr = webdriver.Chrome(options=options)
    dr.get(url)

    # we are performing action here
    print(dr.title)

    # closing the browser
    dr.quit()


if __name__ == "__main__":
    # Our url is defined here
    pageUrl = "https://www.geeksforgeeks.org"
    pageLoad(pageUrl)
