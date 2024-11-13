# import kivy module
import kivy

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require("1.9.1")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button

# This layout allows you to set relative coordinates for children.
from kivy.uix.relativelayout import RelativeLayout


# class in which we are creating the button
class ButtonApp(App):

    def build(self):
        r1 = RelativeLayout()

        # working button
        btn1 = Button(text="Push Me !",
                      font_size="20sp",
                      background_color=(1, 1, 1, 1),
                      color=(1, 1, 1, 1),
                      size=(32, 32),
                      size_hint=(.2, .2),
                      pos=(200, 250))

        # disabled button
        btn2 = Button(text="Disabled:(:( !",
                      font_size="20sp",
                      background_color=(1, 1, 1, 1),
                      color=(1, 1, 1, 1),
                      size=(32, 32),
                      size_hint=(.2, .2),
                      pos=(500, 250),

                      # Add disabled property true to disabled button
                      disabled=True)

        r1.add_widget(btn1)
        r1.add_widget(btn2)

        # bind() use to bind the button to function callback
        btn1.bind(on_press=self.callback)
        return r1

    # callback function tells when button pressed
    def callback(self, event):
        print("button pressed")
        print('Yoooo !!!!!!!!!!!')

    # creating the object root for ButtonApp() class


root = ButtonApp()

# run function runs the whole program
# i.e run() method which calls the target
# function passed to the constructor.
root.run()
