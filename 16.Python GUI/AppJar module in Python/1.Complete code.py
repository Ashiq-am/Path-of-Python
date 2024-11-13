# Python program to demonstrate
# hello world in appjar


# import the library
from appJar import gui

# let app be name of gui
# variable
app = gui()

# Adding the label
app.addLabel("title", " Hello World! ")

# Setting the background color
app.setLabelBg("title", "blue")
app.go()
