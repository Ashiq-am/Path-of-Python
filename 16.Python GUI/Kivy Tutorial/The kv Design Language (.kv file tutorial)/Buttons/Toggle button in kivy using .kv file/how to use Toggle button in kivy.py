# Program to explain how to use Toggle button in kivy

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# The ToggleButton widget acts like a checkbox.
# To use this you must have to import it.
from kivy.uix.togglebutton import ToggleButton

# The GridLayout arranges children in a matrix.
# It takes the available space and divides it
# into columns and rows, then adds
# widgets to the resulting “cells”.
from kivy.uix.gridlayout import GridLayout


# Create the Layout Class
class Toggle_btn(GridLayout):
    pass


# Create the App Class
class ToggleApp(App):
    def build(self):
        return Toggle_btn()

    # Run the App


if __name__ == '__main__':
    ToggleApp().run()
