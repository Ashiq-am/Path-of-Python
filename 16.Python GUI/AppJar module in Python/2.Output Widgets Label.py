# Python program to demonstrate
# label widget of appjar


from appJar import gui

app = gui()

# Adding the label
app.addLabel("label_1",
			text ="This is a label")

app.go()
