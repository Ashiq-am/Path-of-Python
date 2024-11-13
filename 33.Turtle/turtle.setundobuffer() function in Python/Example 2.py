# importing package
import turtle

# print default value
print(turtle.undobufferentries())

# loop for motion
for i in range(50):
    # one statement increase the
    # undobuffer enteries
    turtle.fd(1)

# print undobuffer enteries ie; 50
# due to above loop with one statement
print(turtle.undobufferentries())

# set undobuffer to None
turtle.setundobuffer(None)

# print undobuffer enteries
# i.e; value set by set undobuffer
print(turtle.undobufferentries())
