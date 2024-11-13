# make sure you have installed kivy for this to work
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# if you not import label and use it it through error
from kivy.uix.label import Label

# defining the App class

class MyDemoApp(App):
	def build(self):
		# label display the text on screen
		ll = Label(text="This is a normal label")
		return ll

# creating the object
label = MyDemoApp()
# run the window
label.run()
