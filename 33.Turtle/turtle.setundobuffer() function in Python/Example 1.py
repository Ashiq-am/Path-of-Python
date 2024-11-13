# importing package
import turtle

# check default value of undobuffer
print(turtle.undobufferentries())

# set undo buffer by 10 as value
turtle.setundobuffer(10)

# loop executes 50 times with
# turtle.forward(1) statement
# i.e; undobufferenteries gives 50
for i in range(50):
    turtle.forward(1)

# but gives 10 as it is set already
print(turtle.undobufferentries())
