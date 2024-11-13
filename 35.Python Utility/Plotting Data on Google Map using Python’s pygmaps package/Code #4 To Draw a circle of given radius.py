import pygmaps

mymap4 = pygmaps.maps(30.3164945, 78.03219179999999, 15)

# Draw a circle of given radius
# 1st argument is latitude
# 2nd argument is longitude
# 3rd argument is radius (in meter)
# 4th argument is colour of the circle
mymap4.addradpoint(30.307977, 78.048457, 95, "# FF0000")
mymap4.draw('pygmap4.html')
