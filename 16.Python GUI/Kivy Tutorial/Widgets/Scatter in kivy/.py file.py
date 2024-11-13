# Program to explain how to use Scatter in kivy

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# Scatter is used to build interactive
# widgets that can be translated,
# rotated and scaled with two or
# more fingers on a multitouch system.
from kivy.uix.scatter import Scatter

# Widgets are elements of a
# graphical user interface that
# form part of the User Experience.
from kivy.uix.widget import Widget

# This layout allows you to set relative coordinates for children.
from kivy.uix.relativelayout import RelativeLayout


# Creating widget class
class SquareWidget(Widget):
    pass


# Creating Scatter Class
class ScatterWidget(Scatter):
    pass


# Create the layout class
class Scatter_App(RelativeLayout):
    pass


class ScatterApp(App):
    def build(self):
        return Scatter_App()


if __name__ == '__main__':
    ScatterApp().run()
