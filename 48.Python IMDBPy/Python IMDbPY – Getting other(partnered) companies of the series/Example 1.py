# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6473300"

# getting information
series = ia.get_movie(code)

# getting other companies of the series
companies = series.data['other companies']

# printing the object i.e name
print(series)

# print the companies
print(companies)
