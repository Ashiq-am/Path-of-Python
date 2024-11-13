# In case of an error, try changing the tags used here.

li_tags = experience.find('div')
a_tags = li_tags.find("a")
job_title = a_tags.find("h3").get_text().strip()

print(job_title)

company_name = a_tags.find_all("p")[1].get_text().strip()
print(company_name)

joining_date = a_tags.find_all("h4")[0].find_all("span")[1].get_text().strip()

employment_duration = a_tags.find_all("h4")[1].find_all(
	"span")[1].get_text().strip()

print(joining_date + ", " + employment_duration)
