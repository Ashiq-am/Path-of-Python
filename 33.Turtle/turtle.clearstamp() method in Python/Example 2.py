# import package
import turtle

# list to store ids
import lst as lst

ids = []

# loop to create motion
# with stamps
for i in range(12):
    # motion
    turtle.forward(50)

    # stampid
    id = turtle.stamp()
    lst.append(id)
    turtle.right(30)

# hide the turtle for
# better understandings
turtle.ht()

# loop for clear stamps with
# their ids using clearstamp
# half stamps are cleared
for i in range(len(lst) // 2):
    turtle.clearstamp(lst[i])
