# Program to Show how to create a Progressbar in .kv file

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# The Label widget is for rendering text.
from kivy.uix.label import Label

# The ProgressBar widget is used to
# visualize the progress of some task
from kivy.uix.progressbar import ProgressBar

# BoxLayout arranges children in a vertical or horizontal box.
# or help to put the children at the desired location.
from kivy.uix.boxlayout import BoxLayout


# The class whose internal work is in kv file
class ProgBar(BoxLayout):
    pass


# Create the App Class
class mainApp(App):
    def build(self):
        return ProgBar()

    # Create the run


if __name__ == '__main__':
    mainApp().run()
