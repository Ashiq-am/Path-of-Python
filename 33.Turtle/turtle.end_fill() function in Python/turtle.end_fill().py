# importing package
import turtle

# set turtle position
# and color
turtle.up()
turtle.goto(0,-30)
turtle.down()
turtle.color("yellow")

# start fill block
turtle.begin_fill()

# all instuction within this
# block are filled with turtle
# color as set above
turtle.circle(60)

# end fill block
turtle.end_fill()

# hide the turtle
turtle.hideturtle()
