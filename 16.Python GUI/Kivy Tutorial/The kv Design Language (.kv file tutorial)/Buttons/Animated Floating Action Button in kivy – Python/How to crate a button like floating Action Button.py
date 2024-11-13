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

# The Clock object allows you to
# schedule a function call in the future
from kivy.clock import Clock

# To work with Animation you must have to import it
from kivy.animation import Animation


# creating the root widget used in .kv file
class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Schedule the interval for the animation
        Clock.schedule_interval(self.breath, 1)

    # Creating Animation function name breath
    def breath(self, dtx):
        # create an animation object. This object could be stored
        # and reused each call or reused across different widgets.
        # += is a sequential step
        anim = (Animation(btn_size=(60, 60), t='in_quad', duration=.5) +
                Animation(btn_size=(70, 70), t='in_quad', duration=.5))

        # Call the button id
        tgt = self.ids.cta

        # Start the Animation
        anim.start(tgt)

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
