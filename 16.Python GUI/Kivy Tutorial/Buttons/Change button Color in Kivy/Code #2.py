## Sample Python application demonstrating the
## How to change button color in Kivy.
###################################################

# import kivy module
import kivy

# to choose the colors randomly
# every time you run it shows different color
import random

# this restricts the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button

# BoxLayout arranges children in a vertical or horizontal box.
# or help to put the children at the desired location.
from kivy.uix.boxlayout import BoxLayout

# declaring the colours you can use directly also
red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]


# class in which we are creating the button
class ChangeColorApp(App):

    def build(self):
        superBox = BoxLayout(orientation='vertical')

        HB = BoxLayout(orientation='horizontal')

        # creating the list of defined colors
        colors = [red, green, blue, purple]

        # Changing the color of buttons
        # here you can see how you can change the color
        btn1 = Button(text="One",
                      # Color of button is changed not default
                      background_color=random.choice(colors),
                      font_size=32,
                      size_hint=(0.7, 1))

        btn2 = Button(text="Two",
                      background_color=random.choice(colors),
                      font_size=32,
                      size_hint=(0.7, 1))

        HB.add_widget(btn1)
        HB.add_widget(btn2)

        VB = BoxLayout(orientation='vertical')

        btn3 = Button(text="Three",
                      background_color=random.choice(colors),
                      font_size=32,
                      size_hint=(1, 10))

        btn4 = Button(text="Four",
                      background_color=random.choice(colors),
                      font_size=32,
                      size_hint=(1, 15))

        VB.add_widget(btn3)
        VB.add_widget(btn4)

        superBox.add_widget(HB)
        superBox.add_widget(VB)

        return superBox

    # creating the object root for App class


root = ChangeColorApp()

# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
root.run()
