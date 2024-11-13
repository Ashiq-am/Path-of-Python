# import package
import turtle


# set drawing turtle speed
turtle.speed(10)

# loop for pattern
for i in range(12):
    turtle.circle(50)
    turtle.right(30)



# As simply use of bye() here will shut the
# turtle graphics window too fast so use
# loops to pass the time
for i in range(2000):
    for j in range(500):
        pass

# shut the turtle graphics window
turtle.bye()
