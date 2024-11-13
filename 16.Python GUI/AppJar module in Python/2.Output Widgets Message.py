# Python program to demonstrate
# message widget of appjar


from appJar import gui


app = gui()

# Adding the message label
app.addLabel("label_1",
			text ="This is a message label")

app.go()
