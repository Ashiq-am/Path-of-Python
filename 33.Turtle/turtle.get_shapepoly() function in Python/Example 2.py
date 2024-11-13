# import package
import turtle

# get all shapes
shp=turtle.getshapes()
print(shp)

# loop for getting shapepoly
# of all the shapes
for i in range(len(shp)):
	turtle.shape(shp[i])
	print(turtle.get_shapepoly())
