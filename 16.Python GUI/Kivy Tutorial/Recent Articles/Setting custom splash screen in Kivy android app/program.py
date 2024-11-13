# importing Kivy App
from kivy.app import App

# importing builder from kivy
from kivy.lang import Builder


# this is the main class which
# will render the whole application
class uiApp(App):

	# method which will render our application
	def build(self):
		return Builder.load_string("""
BoxLayout:
	BoxLayout:
	BoxLayout:
		canvas.before:
			Color:
				rgba:[0,1,0,1]
			Rectangle:
				pos:self.pos
				size:self.size
	BoxLayout:
								""")


# running the application
uiApp().run()
