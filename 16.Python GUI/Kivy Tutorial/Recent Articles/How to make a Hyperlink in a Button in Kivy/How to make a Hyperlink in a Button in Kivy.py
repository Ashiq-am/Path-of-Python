# importing button widget from kivy framework
from kivy.uix.button import Button

from kivy.app import App

# importing builder from kivy
from kivy.lang import Builder


# this is the main class which will render the whole application
class uiApp(App):

	# method which will render our application
	def build(self):
		return Builder.load_string(""" 

Button: 

	# text which will appear on button 
	text:"click here to open google search" 

	on_release: 

		# importing webbrowser module 
		import webbrowser 

		# it will open google window in your browser 
		webbrowser.open('http://www.google.com') 

		print("see like this way you can write python supported code in kivy file") 


								""")

# running the application
uiApp().run()
