jobs_html = soup.find_all('a', {'class': 'job-card-list__title'})
# In case of an error, try changing the XPath.

job_titles = []

for title in jobs_html:
	job_titles.append(title.text.strip())

print(job_titles)
