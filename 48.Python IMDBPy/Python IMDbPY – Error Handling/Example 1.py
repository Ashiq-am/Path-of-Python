# importing libraries
from imdb import IMDb, IMDbError

# try block
try:

    # creating instance of imdb
    ia = IMDb()

    # getting person (it accept people id only)
    people = ia.get_person('abcd')

# except block
except IMDbError as e:

    # printing the exception
    print(e)
