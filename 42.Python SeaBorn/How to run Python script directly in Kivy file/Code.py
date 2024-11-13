# importing image widget of kivy framework
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.app import App

# importing boxlayout for our application
from kivy.uix.boxlayout import BoxLayout


# this will connect MainWindow which we have created in ui.kv with main.py file
class MainWindow(BoxLayout):
	pass


"""
Note:- keep in mind that our .kv file name was ui.kv so our rendering class(class which will render our application) name
should be like uiApp otherwise we will not get the desired output!!
"""


# this is the main class which will render the whole application
class uiApp(App):

	# method which will render our application
	def build(self):
		return MainWindow()


# running the application
uiApp().run()
