# importing packages
from kivy.lang import Builder
from datetime import datetime
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker

# writing kv lang
KV = '''
# declaring layout
MDFloatLayout:

	# creating a button
	MDFillRoundFlatButton:
		text: "Set Time"
		pos_hint: {'center_x': .5, 'center_y': .5}

		# creating button event
		# this will trigger time_picker
		on_release: app.time_picker()
'''


# main app class
class Main(MDApp):
    def build(self):
        return Builder.load_string(KV)

    # creating a function for time_picker
    def time_picker(self):
        # converting string to time format
        default_time = datetime.strptime("12:00:00", '%H:%M:%S').time()
        # gets time picker
        t = MDTimePicker()
        # Setting the default time for time picker
        t.set_time(default_time)
        # opens time picker
        t.open()


# running app
Main().run()
