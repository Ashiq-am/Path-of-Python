# Initial job item search dict
details = {}

# Click job item
ele.click()

# Wait job item's title appears in 5 seconds
job_title_ele = _tab.wait_appear(
    locator.chrome.linkedin.jobitem.job_title, wait_timeout=5)

# If job item's title exists, get the title
# string and save into result object 'details'
if job_title_ele:
    details["Job Title"] = job_title_ele.get_text().strip()

# Wait job item's company name appears in 5 seconds
job_company_ele = _tab.wait_appear(
    locator.chrome.linkedin.jobitem.job_company, wait_timeout=2)

# If job item's company name exists, get the company
# name string and save into result object 'details'
if job_company_ele:
    details["Company Name"] = job_company_ele.get_text().strip()

# Wait job item's company scale appears in 5 seconds
company_size_ele = _tab.wait_appear(
    locator.chrome.linkedin.jobitem.company_size, wait_timeout=2)

# If job item's company scale exists, get the
# company scale string and save into result
# object 'details'
if company_size_ele:
    scale = company_size_ele.get_text().strip(
    ) if "employees" in company_size_ele.get_text() else ""
    details["Company Size"] = scale

# Wait job item's post date appears in 5 seconds
job_post_date_ele = _tab.wait_appear(locator.chrome.linkedin.jobitem.job_post_date,
                                     wait_timeout=2)

# If job item's post date exists, get
# the post date string and save into
# result object 'details'
if job_post_date_ele:
    post_date = job_post_date_ele.get_text().strip() \
        if "ago" in job_post_date_ele.get_text() else ""
    details["Post Date"] = post_date

# Wait job item's type appears in 5 seconds
job_type_ele = _tab.wait_appear(locator.chrome.linkedin.jobitem.job_type,
                                wait_timeout=2)

# If job item's type exists, get the type string
# and save into result object 'details'
if job_type_ele:
    details["Job Type"] = job_type_ele.get_text().strip()
