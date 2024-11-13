# import required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import csv
import time

# give name of csv file
filename = "result.csv"

# open file in write mode
f = open(filename, 'w')

# create header
header = "name,status\n"

# write into the file
f.write(header)

# put rollnumber without zero like
# your number 0477593 then
# put 477593 upto XXXXX.
start_roll_no = 477593
end_roll_no = 477599

for i in range(start_roll_no, end_roll_no + 1):

    # exception handling
    try:
        # create instance of Chrome webdriver
        driver = webdriver.Chrome()

        # paste the link upboard website
        driver.get("http://upresults.nic.in/PAHS20SS/HighGetRoll.htm")

        # roll number start with zero then change into string
        tv = '0' + str(i)

        # find the element where we have to
        # enter the xpath target rollnumber box
        # and put rollnumber value who store in t.
        driver.find_element_by_xpath("/html/body/center/table/tbody/tr[2]/td/form/p[1]/input").send_keys(t)

        # paste the xpath of submit button
        driver.find_element_by_xpath("/html/body/center/table/tbody/tr[2]/td/form/p[2]/input[1]").click()

        # name of student's x_path copy and get text of element
        name = driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr[2]/td[2]/p/b/font').text

        # result of student's x_path copy and get text of element
        status = driver.find_element_by_xpath('/html/body/center/table[3]/tbody/tr[5]/td[6]/b/font').text

        # write in the file
        f.write(name + "," + status + "\n")

        # close the web driver
        driver.close()

    # using exception when rollnumber is wrong and
    # not show result on this roll number
    except NoSuchElementException as exception:
        continue

# close and save the file
f.close()
