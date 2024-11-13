# import package
import turtle

# make a turtle object
# and do some drawing
t1 = turtle.Turtle()
t1.up()
t1.setpos(-100, 50)
t1.down()
t1.circle(50)

# make a turtle object
# and do some drawing
t2 = turtle.Turtle()
t2.up()
t2.setpos(50, 50)
t2.down()
t2.circle(50)

# make a turtle object
# and do some drawing
t3 = turtle.Turtle()
t3.up()
t3.setpos(50, -100)
t3.down()
t3.circle(50)

# make a turtle object
# and do some drawing
t4 = turtle.Turtle()
t4.up()
t4.setpos(-100, -100)
t4.down()
t4.circle(50)

# here we clear the work done by turtle
# objects : t1 and t3 only but turtle
# shape remain as it is
t1.clear()
t3.clear()
