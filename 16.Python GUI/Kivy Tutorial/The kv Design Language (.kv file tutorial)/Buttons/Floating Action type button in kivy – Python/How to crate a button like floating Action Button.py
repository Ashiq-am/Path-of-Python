## Sample Python application demonstrating that
## How to crate a button like floating Action Button
## in Kivy using .kv file

###################################################
# import modules

import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# BoxLayout arranges widgets in either
# in a vertical fashion that
# is one on top of another or in a horizontal
# fashion that is one after another.
from kivy.uix.boxlayout import BoxLayout

# To change the kivy default settings
# we use this module config
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)


# creating the root widget used in .kv file
class MainWindow(BoxLayout):
    pass


# creating the App class in which name
# .kv file is to be named main.kv
class MainApp(App):
    # defining build()
    def build(self):
        # returning the instance of root class
        return MainWindow()

    # run the app


if __name__ == '__main__':
    MainApp().run()
