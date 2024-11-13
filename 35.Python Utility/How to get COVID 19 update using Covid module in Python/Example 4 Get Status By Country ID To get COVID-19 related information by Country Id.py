from covid import Covid

covid = Covid()
cases = covid.get_status_by_country_id(18)

print(cases)
