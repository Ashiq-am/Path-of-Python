# main.py file
# program for creating checkbox using .kv in kivy.

# import kivy module
import kivy

# set require version
kivy.require("1.9.0")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

## not necessary while using .kv file
from kivy.uix.checkbox import CheckBox

# To do some manupulation on window impoet window
from kivy.core.window import Window

# Container class for the app's widgets
class SampBoxLayout(BoxLayout):

	# Callback for the checkbox
	def checkbox_click(self, instance, value):
		if value is True:
			print("Checkbox Checked")
		else:
			print("Checkbox Unchecked")


# App derived from App class
class SampleApp(App):
	# build is a method of Kivy's App class used
	# to place widgets onto the GUI.
	def build(self):
		# setting up window background color
		Window.clearcolor = (0, 0, .30, .60)
		return SampBoxLayout()

# Rum the app
root = SampleApp()
root.run()
