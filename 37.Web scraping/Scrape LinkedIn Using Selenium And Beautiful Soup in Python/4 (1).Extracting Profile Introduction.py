# In case of an error, try changing the tags used here.

name_loc = intro.find("h1")

# Extracting the Name
name = name_loc.get_text().strip()
# strip() is used to remove any extra blank spaces

works_at_loc = intro.find("div", {'class': 'text-body-medium'})

# this gives us the HTML of the tag in which the Company Name is present
# Extracting the Company Name
works_at = works_at_loc.get_text().strip()


location_loc = intro.find_all("span", {'class': 'text-body-small'})

# Ectracting the Location
# The 2nd element in the location_loc variable has the location
location = location_loc[1].get_text().strip()

print("Name -->", name,
	"\nWorks At -->", works_at,
	"\nLocation -->", location)
