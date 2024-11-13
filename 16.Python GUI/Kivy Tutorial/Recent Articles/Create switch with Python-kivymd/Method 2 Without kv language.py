# import packages
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.selectioncontrol import MDSwitch

# App class
class MainApp(MDApp):
	def build(self):

		# defining blank screen/layout.
		screen = Screen()

		# defining MDSwitch widget and storing in a variable
		wid = MDSwitch(pos_hint={'center_x': 0.5, 'center_y': 0.5})

		# adding widget to the screen
		screen.add_widget(wid)

		# returns screen/layout
		return screen

# running app
MainApp().run()
