# Importing required modules
from geopy.geocoders import Nominatim
from tkinter import *


# Funtion to get zipcode input
def zip_code():
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        zipcode = str(e.get())
        location = geolocator.geocode(zipcode)
        res.set(location.address)

    except:
        location = "Oops! something went wrong"
        res.set(location)

    # Creating tkinter object


# and background set for light grey
master = Tk()
master.configure(bg='light grey')

# Variable Classes in tkinter
res = StringVar();

# Creating label for each information
Label(master, text="Zipcode: ", bg="light grey").grid(row=0, sticky=W)
Label(master, text="Details of the pincode:", bg="light grey").grid(row=3, sticky=W)

# Creating label for class variable
Label(master, text="", textvariable=res, bg="light grey").grid(row=3, column=1, sticky=W)

e = Entry(master)
e.grid(row=0, column=1)

# Creating a button using the widget
# Button that will call the submit function
b = Button(master, text="Show", command=zip_code)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()
