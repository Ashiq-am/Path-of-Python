# Kivy example for the Popup widget

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

# Widgets are elements of a graphical user
# interface that form part of the User Experience.
from kivy.uix.widget import Widget
# The Label widget is for rendering text.
from kivy.uix.label import Label

# module consist the floatlayout
# to work with FloatLayout first
# you have to import it
from kivy.uix.floatlayout import FloatLayout

# Popup widget is used to create popups.
# By default, the popup will cover
# the whole “parent” window.
# When you are creating a popup,
# you must at least set a Popup.title and Popup.content.
from kivy.uix.popup import Popup


# Creating a widget class
# through this we add button
# the commands of the class is in .kv file
class Widgets(Widget):
    def btn(self):
        # calling of the show popup function
        show_popup()

    # Popup class is defined


# The command of the class is in .kv file
class Popups(FloatLayout):
    pass


# create App class
class MyApp(App):
    def build(self):
        # return the widget
        return Widgets()

    # define popup function in this we create the popup


def show_popup():
    show = Popups()

    popupWindow = Popup(title="Popup Window", content=show,
                        size_hint=(None, None), size=(200, 200))

    # open popup window
    popupWindow.open()


# Attach close button press with popup.dismiss action
# content.bind(on_press = popup.dismiss)


# run the App
if __name__ == "__main__":
    MyApp().run()
