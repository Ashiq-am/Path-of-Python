# importing packages
from datetime import datetime
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.pickers import MDTimePicker

# app class
class MainApp(MDApp):

	# defining app
	def build(self):
		# calling screen
		screen = Screen()

		# converting string to time format
		previous_time = datetime.strptime("12:00:00", '%H:%M:%S').time()

		# calling MDTimePicker
		t = MDTimePicker()

		# setting up default time
		t.set_time(previous_time)

		# opens Time picker
		t.open()

		# returing screen
		return screen


# running app
MainApp().run()
