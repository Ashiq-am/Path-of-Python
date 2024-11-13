from logging import root
from tkinter import Image, Label

from PIL import ImageTk


def openfilename():
    pass


def open_img():
    # Select the Imagename from a folder
    x = openfilename()

    # opens the image
    img = Image.open(x)

    # resize the image and apply a high-quality down sampling filter
    img = img.resize((250, 250), Image.ANTIALIAS)

    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)

    # create a label
    panel = Label(root, image=img)

    # set the image as img
    panel.image = img
    panel.grid(row=2)








"""The openfilename function will return the file name of image"""
