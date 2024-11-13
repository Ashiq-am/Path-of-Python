# Simple program to show how we add AsyncImage in kivy App

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# The Image widget is used to display an image
# this module contains all features of images
from kivy.uix.image import AsyncImage


# creating the App class
class MyApp(App):

    # defining build()

    def build(self):
        # return image
        return AsyncImage(source='http://kivy.org/logos/kivy-logo-black-64.png')

    # run the App


MyApp().run()







'''How can we add AsyncImage i.e. from the webserver(external)'''