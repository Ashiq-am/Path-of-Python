# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# name of the person
company_name = "Alt Bala ji"

# searchning the name of the person
search = ia.search_company(company_name)

# printing the result
print(search)
