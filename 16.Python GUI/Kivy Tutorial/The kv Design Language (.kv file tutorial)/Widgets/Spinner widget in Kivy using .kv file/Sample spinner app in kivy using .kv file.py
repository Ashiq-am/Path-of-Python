# Sample spinner app in kivy using .kv file

# to change the kivy default settings we use this module config
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)

# Program to Show how to create a switch
# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# Spinner is a widget that provides a
# quick way to select one value from a set.
# like a dropdown list
from kivy.uix.spinner import Spinner

# module consists the floatlayout
# to work with FloatLayout first
# you have to import it
from kivy.uix.floatlayout import FloatLayout

# Here for providing colour to the background
from kivy.core.window import Window


# create LayoutClass
class SampBoxLayout(FloatLayout):
    # For Spinner defining spinner clicked function
    def spinner_clicked(self, value):
        print("Language selected is " + value)

    # # Make an App by deriving from the App class


class SampleApp(App):
    def build(self):
        # Set the background color for the window
        Window.clearcolor = (0.555, 0.261, .888, 0.5)
        return SampBoxLayout()

    # create object for thje Appclass


root = SampleApp()
# run the class
root.run()

