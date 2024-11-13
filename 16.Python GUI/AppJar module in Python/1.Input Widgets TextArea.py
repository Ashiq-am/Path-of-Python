# Python program to demonstrate
# textarea widget appjar


from appJar import gui


app = gui()

# Adding text area
app.addTextArea("TA_1")

# Setting the default value
app.setTextArea("TA_1",
				"This is a Text field",
				end = True, callFunction = False)

app.go()
