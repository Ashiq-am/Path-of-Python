# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6473300"

# getting information
series = ia.get_movie(code)

# adding new info set
ia.update(series, 'episodes')

# getting episodes of the series
episodes = series.data['episodes']

# printing the object i.e name
print(series)

print("=========")

# traversing each key
for i in episodes.keys():

    # printing season number
    print("Season" + str(i))

    # traversing season i
    for j in episodes[i]:
        # getting year of episode
        year = episodes[i][j]['year']

        # printing title
        print(" Ep " + str(j) + " year : " + str(year))
