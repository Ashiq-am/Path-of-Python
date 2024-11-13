from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def pageLoad(url):
    dr = webdriver.Chrome()
    dr.get(pageUrl)
    wait = 5
    try:
        # Checking our desired element is loaded or not
        element = WebDriverWait(dr, wait).until(
            ec.presence_of_element_located((By.CSS_SELECTOR,
                                            '.HomePageTopicCard_homePageTopicCard__eePhS.row2')))
        print("You can procced to scrape the data.....\n")

        # We are now performing actions with our desired element
        c = 1
        print("Our Web Dev Courses :-")
        for i in dr.find_elements(By.CSS_SELECTOR,
                                  '.HomePageTopicCard_homePageTopicCard__eePhS.row2 '):
            print(str(c) + ". ", i.text)
            c += 1
    except TimeoutException:
        # If our desired element is not found
        print("An ERROR Occured!!!!")

    dr.quit()


if __name__ == "__main__":
    # our url in which we want to visit and perform actions
    pageUrl = "https://www.geeksforgeeks.org"
    pageLoad(pageUrl)
