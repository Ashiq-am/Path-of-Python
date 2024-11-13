# Here we set range(1,11) to get top
# 10 jobs, it can be set with any value
for i in range(1, 11):

	# Wait the job item appears in 5 second,
	# and get the element with index value
	ele = _tab.wait_appear(locator.chrome.linkedin.jobitem.job_listitem, {
						"index": i}, wait_timeout=5)
