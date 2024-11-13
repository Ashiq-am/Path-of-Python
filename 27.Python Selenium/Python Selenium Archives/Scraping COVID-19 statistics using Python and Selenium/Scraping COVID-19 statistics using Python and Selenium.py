from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome("C:/chromedriver.exe")
driver.get("https://www.covid19india.org/")
sleep(2)


def extractor():
	TCases = driver.find_element_by_xpath(
		"/html / body / div / div / div[2]/div[1]/div[2]/div[1]/h1 / span")
	TActive = driver.find_element_by_xpath(
		"/html / body / div / div / div[2]/div[1]/div[2]/div[2]/h1 / span")
	TRecov = driver.find_element_by_xpath(
		"/html / body / div / div / div[2]/div[1]/div[2]/div[3]/h1 / span")
	TDeath = driver.find_element_by_xpath(
		"/html / body / div / div / div[2]/div[1]/div[2]/div[4]/h1 / span")
	New_Cases = driver.find_element_by_xpath(
		"/html / body / div / div / div[2]/div[1]/div[2]/div[1]/h4 / span")
	New_Rcov = driver.find_element_by_xpath(
		"/html / body / div / div / div[2]/div[1]/div[2]/div[3]/h4 / span")
	New_Death = driver.find_element_by_xpath(
		"/html / body / div / div / div[2]/div[1]/div[2]/div[4]/h4 / span")

	print("Total Cases:", TCases.text)
	print("Total Active Cases:", TActive.text)
	print("Total Recovered Cases:", TRecov.text)
	print("Total Deaths:", TDeath.text)
	print("New Cases:", New_Cases.text[1:len(New_Cases.text)-1])
	print("New Recovered Cases:", New_Rcov.text[1:len(New_Rcov.text)-1])
	print("Additional Deaths yet:", New_Death.text[1:len(New_Death.text)-1])


while True:
	extractor()
	sleep(60 * 60)
