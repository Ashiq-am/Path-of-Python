company_name_html = soup.find_all(
'div', {'class': 'job-card-container__company-name'})
company_names = []

for name in company_name_html:
	company_names.append(name.text.strip())

print(company_names)
