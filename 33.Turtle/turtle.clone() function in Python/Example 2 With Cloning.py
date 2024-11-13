# import package
import turtle


# make first turtle object
tur1=turtle.Turtle()

# set turtle properties
tur1.width(5)
tur1.color("red")

# move it
tur1.circle(50)

# make another turtle object
tur2=turtle.Turtle()

# cloning the properties of
# first turtle object
tur2 = tur1.clone()

# move it
tur2.circle(-50)
