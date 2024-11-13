# Library for web automation apis
# Locator used for selector reference
from clicknium import clicknium as cc, locator

# Library for delay function
from time import sleep

# Library for save dict list data into csv file
from csvutils import list_dict_to_csv

# Library for clear clipboard and get clipboard data
from clipboard import get_clipboard_data, clear_clipboard_data

# Library for get setting in 'setting.json' file
from setting import Setting


# Login to LinkedIn page
# Find input box for username and password,
# and fill in with the value in setting.json
# Find submit button, and click it to login
# Wait 'skip add phone' button if it needs,
# and click the 'skip' button
def login():
    # Find input box for username
    # Fill in with the key value
    # 'linkedin_login_name' in setting.json
    _tab.find_element(locator.chrome.linkedin.login.login_email).set_text(
        Setting.login_name)

    # Find input box for password
    # Fill in with the key value
    # 'linkedin_login_password' in setting.json
    _tab.find_element(locator.chrome.linkedin.login.login_password).set_text(
        Setting.login_password)

    # Find submit button, and click it to login
    _tab.find_element(locator.chrome.linkedin.login.signin).click()

    # Wait skip add phone button appears in 5
    # seconds, if it exists, click the 'skip' button
    _tab.wait_appear(
        locator.chrome.linkedin.login.skip_add_phone, wait_timeout=5).click()


def search_jobs():
    # Wait the page load completely after
    # submitting login information
    # Find job channel and click it to
    # switch to job channel
    _tab.wait_appear(locator.chrome.linkedin.job.jobs_channel,
                     wait_timeout=5).click()

    # Wait job search keyword input box exists
    # in 10 seconds If exists fill in with
    # the key value 'linkedin_search_job_key'
    # in setting.json
    _tab.wait_appear(locator.chrome.linkedin.job.job_search_key,
                     wait_timeout=10).set_text(Setting.search_job_key)

    # Find job search location input box
    # Fill in with the key value
    # 'linkedin_search_job_location' in setting.json
    _tab.find_element(locator.chrome.linkedin.job.job_search_location).set_text(
        Setting.search_job_location)

    # Find the search button, and click it to search
    _tab.find_element(locator.chrome.linkedin.job.job_search).click()


# Scrape the information of the top 10 jobs
# For each job item, get the title,
# the company name, the size of the company,
# the post date, the job type
# Save search results into csv file
def get_job_top10_list():
    # Initial search result list
    job_list = []

    # Clear clipboard data first
    clear_clipboard_data()

    # Here we set range(1,11) to get top 10 jobs,
    # it can be set with any value
    for i in range(1, 11):

        # Wait the job item appears in 5 second,
        # and get the element with index value
        ele = _tab.wait_appear(locator.chrome.linkedin.jobitem.job_listitem, {
            "index": i}, wait_timeout=5)

        # If job item exists, click the job
        # item to get detail information
        if ele:
            # Initial job item search dict
            details = {}

            # Click job item
            ele.click()

            # Wait job item's title appears in 5 seconds
            job_title_ele = _tab.wait_appear(
                locator.chrome.linkedin.jobitem.job_title, wait_timeout=5)

            # If job item's title exists, get
            # the title string and save into
            # result object 'details'
            if job_title_ele:
                details["Job Title"] = job_title_ele.get_text().strip()

            # Wait job item's company name appears in 5 seconds
            job_company_ele = _tab.wait_appear(
                locator.chrome.linkedin.jobitem.job_company, wait_timeout=2)

            # If job item's company name exists
            # , get the company name string and
            # save into result object 'details'
            if job_company_ele:
                details["Company Name"] = job_company_ele.get_text().strip()

            # Wait job item's company scale appears in 5 seconds
            company_size_ele = _tab.wait_appear(
                locator.chrome.linkedin.jobitem.company_size, wait_timeout=2)

            # If job item's company scale exists,
            # get the company scale string and
            # save into result object 'details'
            if company_size_ele:
                scale = company_size_ele.get_text().strip(
                ) if "employees" in company_size_ele.get_text() else ""
                details["Company Size"] = scale

            # Wait job item's post date appears in 5 seconds
            job_post_date_ele = _tab.wait_appear(
                locator.chrome.linkedin.jobitem.job_post_date, wait_timeout=2)

            # If job item's post date exists,
            # get the post date string and save
            # into result object 'details'
            if job_post_date_ele:
                post_date = job_post_date_ele.get_text().strip(
                ) if "ago" in job_post_date_ele.get_text() else ""
                details["Post Date"] = post_date

            # Wait job item's type appears in 5 seconds
            job_type_ele = _tab.wait_appear(
                locator.chrome.linkedin.jobitem.job_type, wait_timeout=2)

            # If job item's type exists, get the
            # type string and save into result
            # object 'details'
            if job_type_ele:
                details["Job Type"] = job_type_ele.get_text().strip()

            # Wait job item's share button appears in 5 seconds
            job_share_btn_ele = _tab.wait_appear(
                locator.chrome.linkedin.jobitem.share_button, wait_timeout=2)

            # If job item's share button exists,
            # click the share button
            if job_share_btn_ele:
                job_share_btn_ele.click()

                # Wait the copy link button appears in 5 seconds
                copy_link = _tab.wait_appear(
                    locator.chrome.linkedin.jobitem.copy_link, wait_timeout=2)

                # If the copy link exists, click the copy
                # link to set clipboard data
                if copy_link:
                    copy_link.click()

                    # Sleep 0.2 second to wait the clipboard in ready state
                    sleep(0.2)

                    # Get the job link string and save
                    # into result object 'details'
                    details["Job Link"] = get_clipboard_data()

            # Save job item's result to list object
            job_list.append(details)

    # If it has any results, save into the csv file,
    # set the file path with the key
    # value 'result_csv_file' in setting.json
    if job_list:
        list_dict_to_csv(job_list, Setting.result_csv_file)


if __name__ == "__main__":

    # Create a browser instance with "cc.chrome",
    # for edge browser using "cc.edge"
    # Open browser with specified url and get browser tab
    # For default, it will wait the page load
    # completely. You do not need to add extra time.sleep()
    _tab = cc.chrome.open("https://www.linkedin.com/", is_wait_complete=True)

    # Check whether it needs to login in with username and password
    # True: means it needs to login in with username and password
    # False: means the website has remember authentication information
    if _tab.is_existing(locator.chrome.linkedin.login.login_email):
        # Login to LinkedIn
        login()

    # Search jobs with the keyword and location
    search_jobs()

    # Get top 10 jobs information from search
    # results and save into csv file
    get_job_top10_list()
