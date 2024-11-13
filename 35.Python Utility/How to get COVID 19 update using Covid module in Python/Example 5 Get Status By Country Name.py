from covid import Covid

covid = Covid()
italy_cases = covid.get_status_by_country_name("italy")

print(italy_cases)
