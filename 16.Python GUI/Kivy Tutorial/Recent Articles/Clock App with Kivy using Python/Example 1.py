# importing modules

# it will allow us to get time
import time

# The App class is the base for
# creating Kivy applications
from kivy.app import App

# it will allow us to make interval calls
from kivy.clock import Clock

# Label widget will be used to render text
from kivymd.uix.label import Label

# we will be using this to resize app window
from kivy.core.window import Window

# it will allow us to creat layouts
from kivy.uix.boxlayout import BoxLayout

# declaring window size
Window.size = (400, 700)


# clock class
class myclock(Label):
    def update(self, *args):
        # get the current local time
        self.text = time.asctime()


# App class
class TimeApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # it will create vertical layouts in app

        # calling clock class for time
        clock1 = myclock()

        # updates time with the interval of 1 sec
        Clock.schedule_interval(clock1.update, 1)

        # adding layout to the screen
        layout.add_widget(clock1)

        # adding text to screen
        layout.add_widget(Label(text='INDIA'))

        return layout


root = TimeApp()
root.run()  # running the app
