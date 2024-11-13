from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import getpass

# intializing the driver
driver = webdriver.Chrome(
    executable_path='/usr/lib/chromium-browser/chromedriver')

# directing to the twitter login page
driver.get('https://twitter.com/login')
driver.maximize_window()

# asking the user for username and pas
username = input('Enter Your Username: ')
password = getpass.getpass(prompt='Enter Your Password: ')

# locating the input box for username
u = driver.find_element_by_xpath('//*[@id="react-root"]\
/div/div/div[2]/main/div/div/div[2]/form/div/div[1]\
/label/div/div[2]/div/input')

# inputing the username
u.send_keys('' + str(username) + '')

# locating the input box for password
p = driver.find_element_by_xpath('//*[@id="react-root"]\
/div/div/div[2]/main/div/div/div[2]/form/div/div[2]\
/label/div/div[2]/div/input')

# inputing the password
p.send_keys('' + str(password) + '')
print("loading... \n")
time.sleep(3)

# logging in
driver.find_element_by_xpath('//*[@id="react-root"]\
/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()
time.sleep(10)

# Locating the search box
srch = driver.find_element_by_xpath('//*[@id="react-root"]\
/div/div/div[2]/main/div/div/div/div[2]/div/div[2]\
/div/div/div/div[1]/div/div/div/form/div[1]\
/div/label/div[2]/div/input')

# inputing the hashtag to retweet
s = input('Enter the Hashtag you want to retweet: ')

# inputing the hashtag
srch.send_keys('#' + str(s) + '')

# searching for the hashtag
srch.send_keys(Keys.ENTER)

# inputing maximum number of tweets one wants to retweet
c = int(input('Max no. of Retweets: '))
driver.implicitly_wait(5)

# directing the most latest tweets
driver.find_element_by_xpath('//*[@id="react-root"]/div/\
div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/\
nav/div/div[2]/div/div[2]/a').click()
time.sleep(10)

while (1):
    time.sleep(5)

    # locating the retweet option in the webpage
    rt = driver.find_elements_by_css_selector(
        '.css-18t94o4[data-testid ="retweet"]')
    for r in rt:
        try:

            # retweeting
            r.click()
            time.sleep(2)

            # toggling the confirmation to retweet
            driver.find_element_by_xpath('//*[@id="layers"]/div[2]\
			/div/div/div/div[2]/div[3]/div/div/div/div').click()
            c -= 1
            time.sleep(2)
            if (c == 0):
                break  # breaking from the retweet loop
        except (ElementClickInterceptedException, StaleElementReferenceException):
            pass

    # scrolling to the bottom of the page
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # max number of retweets are achieved
    if (c == 0):
        break  # breaking from the retweet loop
driver.close()
