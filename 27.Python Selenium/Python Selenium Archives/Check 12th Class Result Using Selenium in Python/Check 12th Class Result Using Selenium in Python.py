# import required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import csv
import time

# give name of csv file
filename = "abc.csv"

# open file in write mode
f = open(filename, 'w')

# creat header in file
header = "NAME,STATUS,DIV,NUM\n"

# write into the file
f.write(header)

# put rollnumber without zero like
# your number 0477593 then
# put 477593 upto XXXXX.
start_rollNum = 926840
end_rollNum = 926841

# put range of rollnumber
for i in range(start_rollNum, end_rollNum):

    # use try and except because if any rollnumber
    # is invalid then whole program is not stop.
    try:
        driver = webdriver.Chrome()

        # link is given above copy and paste
        driver.get("https://results.upmsp.edu.in/ResultIntermediate.aspx")

        # add zero in rollnumber in starting
        t = '0' + str(i)

        # district xpath
        state = driver.find_element_by_xpath('//*[@id="ctl00_cphBody_ddl_districtCode"]')
        drp1 = Select(state)

        # select district
        drp1.select_by_visible_text('LUCKNOW')

        # put rollnumber
        driver.find_element_by_xpath('//*[@id="ctl00_cphBody_txt_RollNumber"]').send_keys(t)

        # view result xpath
        driver.find_element_by_xpath('//*[@id="ctl00_cphBody_btnSubmit"]').click()

        # student name
        name = driver.find_element_by_xpath('//*[@id="ctl00_cphBody_lbl_C_NAME"]').text

        # status pass or fail
        status = driver.find_element_by_xpath('//*[@id="ctl00_cphBody_lbl_RESULT"]').text

        # division
        div = driver.find_element_by_xpath('//*[@id="ctl00_cphBody_lbl_DIVISION"]').text

        # obatin marks
        num = driver.find_element_by_xpath('//*[@id="ctl00_cphBody_lbl_MRK_OBT"]').text

        # all details fill into csv file
        f.write(name + "," + status + "," +
                div[1:] + "," + num + "\n")

        # close the driver
        driver.close()

    except NoSuchElementException as exception:
        continue

# close and save the file
f.close()
