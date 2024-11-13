# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6468322"

# getting information
series = ia.get_movie(code)

# adding new info set
ia.update(series, 'episodes')

# getting episodes of the series
episodes = series.data['episodes']

# printing the object i.e name
print(series)

# printing total episodes of each season
# traversing each key
for i in episodes.keys():
    # getting total episode in season i
    n = len(episodes[i])

    # printing total episodes
    print("Total Episodes in Season " + str(i) + " : " + str(n))
