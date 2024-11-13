## Sample Python application demonstrating the
## working of FloatLayout in Kivy using .kv file

###################################################
# import modules

import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# module consist the floatlayout
# to work with FloatLayout first
# you have to import it
from kivy.uix.floatlayout import FloatLayout

# To change the kivy default settings
# we use this module config
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)


# creating the root widget used in .kv file
class FloatLayout(FloatLayout):
    pass


# creating the App class in which name
# .kv file is to be named Float_Layout.kv
class Float_LayoutApp(App):
    # defining build()
    def build(self):
        # returning the instance of root class
        return FloatLayout()

    # run the app


if __name__ == "__main__":
    Float_LayoutApp().run()
