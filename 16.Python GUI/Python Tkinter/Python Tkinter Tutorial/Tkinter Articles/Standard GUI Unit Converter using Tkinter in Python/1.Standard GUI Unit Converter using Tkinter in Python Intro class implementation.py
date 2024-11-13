# import required modules
from tkinter import *
import tkinter as tk
from tkinter.ttk import Progressbar
from time import sleep
import webbrowser


# create intro class .
import wind as wind
from Tools.demo.ss1 import center
from pandas.core.array_algos.transforms import shift


class intro():
    # constructor
    def __init__(self):
        # Used to open the hidden window.
        wind.deiconify()

        wind.resizable(0, 0)

        # Light blue background.
        wind.configure(bg="#008080")

        # Replace the title with your own name.
        wind.title("GeeksforGeeks Unit Converter")

        # window icon.
        icon = PhotoImage(file=r"convert.png")
        wind.iconphoto(False, icon)

        # calling center function to center
        # the window to the screen.
        center(wind, 500, 230)

        # Welcome Label.
        # You can change the welcome text here too.
        entry = Label(wind, bg="#008080", fg="white",
                      text="Welcome to GeeksforGeeks Unit Converter!",
                      font=("Footlight MT Light", 15, "bold"))

        entry.place(x=50, y=30, width=410, height=30)

        # Loading Bar Intialisation.
        self.load = Progressbar(wind, orient=HORIZONTAL,
                                length=250,
                                mode='indeterminate')

        # Start Button that opens
        # converter window.
        self.start = Button(wind, bg="#f5f5f5", fg="black",
                            text="START", command=self.loading)

        self.start.place(x=200, y=90,
                         width=80, height=30)

        # Follow Me Label.
        follow = Label(wind, bg="#008080", fg="white",
                       text="Follow Me On",
                       font=("Helvetica", 12, "bold"))

        follow.place(x=186, y=150, width=104,
                     height=20)

        # Author Social Media links and replace
        # the below 'xxxx' with your profile links.
        self.git = PhotoImage(file=r'gforg.png')
        github = Button(wind, image=self.git, bg="white",
                        relief=FLAT,
                        command=lambda: self.links("xxxx"),
                        cursor="hand2")

        github.place(x=110, y=190, width=30,
                     height=30)

        # Instagram Button.
        self.instag = PhotoImage(file=r'ins.png')

        insta = Button(wind, image=self.instag,
                       bg="#008080", relief=FLAT,
                       command=lambda: self.links("xxxx"),
                       cursor="hand2")

        insta.place(x=190, y=190, width=30,
                    height=30)

        # Facebook Button.
        self.fcb = PhotoImage(file=r'fb.png')

        fb = Button(wind, image=self.fcb, bg="white",
                    relief=FLAT,
                    command=lambda: self.links("xxxxx"),
                    cursor="hand2")

        fb.place(x=270, y=190, width=30,
                 height=30)

        # Twitter Button.
        self.tweet = PhotoImage(file=r'twitter.png')

        twitter = Button(wind, image=self.tweet,
                         bg="white", relief=FLAT,
                         command=lambda: self.links("xxxx"),
                         cursor="hand2")
        twitter.place(x=350, y=190,
                      width=30, height=30)

    # Opening author links in browser.
    def links(self, url):
        webbrowser.get("C:/Program Files" +
                       " (x86)/Google/Chrome/Application/chrome.exe" +
                       " %s --incognito").open(url)

    # Loading ProgressBar.
    def loading(self):
        # Removing start button.
        self.start.place(x=0, y=0, width=0,
                         height=0)
        self.load.place(x=120, y=100)
        # To remove self.start button when loading self.starts
        wind.update()

        c = 0

        while (c100):
            # Calling Shift function
            # to intialise converter window.
            shift("Length")
