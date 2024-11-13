# Python program to activate menu and toolbar
# with keyboard shortcut key

# Import the libraries tkinter and ttk
from tkinter import *
from tkinter import ttk

# Create a GUI app
app = Tk()

# Setting the title and geomtry of the app
app.title('Vinayak App')
app.geometry('600x400')


# Creating function for menu bar
def menubar_shortcut(event=None):
    menubar = Menu()

    # Declare file and edit for showing in menu bar
    file = Menu(menubar, tearoff=False)
    edit = Menu(menubar, tearoff=False)

    # Display file and edit declared in previous step
    menubar.add_cascade(label='File', menu=file)
    menubar.add_cascade(label='Edit', menu=edit)

    # Display of menu bar in the app
    app.config(menu=menubar)


# Creating function for tool bar
def toolbar_shortcut(event=None):
    # Creating and displaying label for toolbar
    toolbar = ttk.Label(app)
    toolbar.pack(side=TOP, fill=X)

    # Creating and displaying of Bold button
    bold_btn = ttk.Button(toolbar, text="Bold")
    bold_btn.grid(row=0, column=0, padx=5)

    # Creating and displaying of italic button
    italic_btn = ttk.Button(toolbar, text="Italic")
    italic_btn.grid(row=0, column=1, padx=5)


# Set up shortcut key for menu bar
app.bind('<Control-p>', menubar_shortcut)

# Set up shortcut key for tool bar
app.bind('<Control-q>', toolbar_shortcut)

# Make the loop for displaying app
app.mainloop()
