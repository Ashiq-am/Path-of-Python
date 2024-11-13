## Sample Python application demonstrating the
## How to set button size and position in Kivy using .kv file

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


# creating the root widget used in .kv file
class FloatLayout(FloatLayout):
    pass


# creating the App class in which name
# .kv file is to be named Float_Layout.kv
class BtnApp(App):
    # defining build()
    def build(self):
        # returning the instance of root class
        return FloatLayout()

    # run the app


if __name__ == "__main__":
    BtnApp().run()
