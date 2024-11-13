# importing pygmaps
import pygmaps

mymap2 = pygmaps.maps(30.3164945, 78.03219179999999, 15)

# draw grids on the map
# 1st argument is the starting point of latitude
# 2nd argument is the ending point of latitude
# 3rd argument is grid size in latitude
# 4th argument is the starting point of longitude
# 5th argument is the ending point of longitude
# 6th argument is grid size in longitude
mymap2.setgrids(30.31, 30.32, 0.001,
                78.04, 78.03, 0.001)

mymap2.draw('pygmap2.html')
