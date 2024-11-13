# python program
# import for turtle module
import turtle

# defining instance of turtle
pen = turtle.Turtle()
head = turtle.Turtle()
head.penup()
head.hideturtle()
head.goto(0, 260)
head.write("This is to display the coordinates of the position where mouse is clicked",
           align="center",
           font=("courier", 12, "normal"))

# giving circle shape to pen i.e. instance of turtle
pen.shape("circle")

# giving colour to turtle
pen.color("red")


# define function to make the turtle move
# to the position which is clicked by the mouse
def btnclick(x, y):
    pen.goto(x, y)
    head.clear()
    head.write(f"x coordinate = {x}, y coordinate = {y}",
               align="center", font=("courier", 24, "normal"))


# this function will call btnclick whenever mouse is clicked
turtle.onscreenclick(btnclick, 1)
turtle.listen()
