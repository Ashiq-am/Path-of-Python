# importing package
import turtle

# print default value
print(turtle.resizemode())

# change mode to auto and check
turtle.resizemode(rmode="auto")
print(turtle.resizemode())

# change mode to user and check
turtle.resizemode(rmode="user")
print(turtle.resizemode())
