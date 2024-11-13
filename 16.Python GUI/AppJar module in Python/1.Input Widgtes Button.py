# Python program to demonstrate
# button widget of appjar


from appJar import gui


# Function to be passed
# when the button is clicked
def clicked(btn):
	print(btn)

app = gui()

# Adding the button
app.addButton("btn_one", clicked)

# Change the name of the button
app.setButton("btn_one", "Click me")

app.go()
