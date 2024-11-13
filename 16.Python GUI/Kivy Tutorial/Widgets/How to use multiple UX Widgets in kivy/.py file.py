# Program to Show how to use multiple UX widget

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# Here for providing colour to the background
from kivy.core.window import Window

# Setting the window size
Window.size = (1120, 630)


# Add the App class
class ClassiqueApp(App):
    def build(FloatLayout):
        pass


# Run the App
if __name__ == '__main__':
    ClassiqueApp().run()
