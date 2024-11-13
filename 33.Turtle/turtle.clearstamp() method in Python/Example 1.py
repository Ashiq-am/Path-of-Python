# import package
import turtle


# set turtle speed to slowest
# for better understandings
turtle.speed(1)

# motion with stamps
# and their ids
turtle.forward(50)
id1 = turtle.stamp()

turtle.forward(50)
id2 = turtle.stamp()

turtle.forward(50)
id3 = turtle.stamp()

# hide the turtle to
# clarify stamps
turtle.ht()

# clear the stamps
# of id : id1 and id3
turtle.clearstamp(id1)
turtle.clearstamp(id3)
