# Import Required Modules
from tkinter import *

# Create Object
root = Tk()

# Set geometry
root.geometry('400x200')

# Add Label
Label(root, text="Youtube Playlist Downloader",
	font="italic 15 bold").pack(pady=10)
Label(root, text="Enter Playlist URL:-", font="italic 10").pack()

# Add Entry box
playlistId = Entry(root, width=60)
playlistId.pack(pady=5)

download_start = Button(root, text="Download Start")
download_start.pack(pady=10)

# Execute Tkinter
root.mainloop()
