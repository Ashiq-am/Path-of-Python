# Wait the page load completely
# after submitting login information
# Find job channel and click it
# to switch to job channel
_tab.wait_appear(locator.chrome.linkedin.job.jobs_channel,
				wait_timeout=5).click()

# Wait job search keyword input
# box exists in 10 seconds
# If exists fill in with the key
# value 'linkedin_search_job_key'
# in setting.json
_tab.wait_appear(locator.chrome.linkedin.job.job_search_key,
				wait_timeout=10).set_text(Setting.search_job_key)

# Find job search location input box
# Fill in with the key value
# 'linkedin_search_job_location' in setting.json
_tab.find_element(locator.chrome.linkedin.job.job_search_location).set_text(
	Setting.search_job_location)

# Find the search button, and click
# it to search
_tab.find_element(locator.chrome.linkedin.job.job_search).click()
