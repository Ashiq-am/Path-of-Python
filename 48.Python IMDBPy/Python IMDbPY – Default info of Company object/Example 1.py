# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# ID
code = "0051941"

# searching the Id
company = ia.get_company(code)

# getting default info
info = company.default_info

# printing name
print(company['name'])

# printing the info
print(info)
