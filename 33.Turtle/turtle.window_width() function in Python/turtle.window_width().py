# import package
import turtle

# get turtle window width
print(turtle.window_width())

# make screen object
# then set size and color
sc = turtle.Screen()
sc.setup(300,300)
sc.bgcolor("green")

# get turtle window width
print(turtle.window_width())

# loops for pass time
for i in range(5000):
    for j in range(5000):
        pass

# set size and color again
sc.setup(500,400)
sc.bgcolor("red")

# get turtle window width
print(turtle.window_width())
