'''Now How can we change the color of canvas by any action so below is the example of in which by
clicking the color of screen changes.'''







# import kivy module
import kivy

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# From graphics module we are importing
# Rectangle and Color as they are
# basic building of canvas.
from kivy.graphics import Rectangle, Color

# The ButtonBehavior mixin class provides Button behavior.
from kivy.uix.button import ButtonBehavior

# The Label widget is for rendering text.
from kivy.uix.label import Label


# class in which we are creating the canvas
class CanvasWidget(ButtonBehavior, Label):
    pass


# Create the App Class
class CanvasApp(App):
    def build(self):
        return CanvasWidget()

    # run the App


CanvasApp().run()
