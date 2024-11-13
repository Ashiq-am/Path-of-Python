# import required package
import pygmaps

# maps method return map object
# 1st argument is center latitude
# 2nd argument is center longitude
# 3ed argument zoom level
mymap1 = pygmaps.maps(30.3164945, 78.03219179999999, 15)

# create the HTML file which includes
# google map. Pass the absolute path
# as an argument.
mymap1.draw('pygmap1.html')
