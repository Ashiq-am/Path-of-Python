# How to use Accordion in kivy using .kv file

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

# The Accordion widget is a form of menu
# where the options are stacked either vertically
# or horizontally and the item in focus
# (when touched) opens up to display its content.
from kivy.uix.accordion import Accordion


# Create the Accordion class
# Whose work is done in .kv file
class Accor(Accordion):
    pass


# Create App class
class AccorApp(App):
    def build(self):
        return Accor()

    # run the App


if __name__ == '__main__':
    AccorApp().run()
