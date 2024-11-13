# Python program to demonstrate
# entry widget appjar


from appJar import gui

app = gui()

# Adding the entry
app.addEntry("entry_1")

# Setting the default value
app.setEntryDefault("entry_1","This is an Entry field")

app.go()
