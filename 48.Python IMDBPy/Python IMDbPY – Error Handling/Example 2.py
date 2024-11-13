# importing libraries
from imdb import IMDb, IMDbError

# try block
try:

    # creating instance of imdb
    ia = IMDb()

    # searching person
    people = ia.search_person('abcd')

# except block
except IMDbError as e:

    # printing the exception
    print(e)
