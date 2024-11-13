# importing packages
from kivy.lang import Builder
from kivymd.app import MDApp

# writing kv lang
KV = '''
MDScreen:

	# designing spinner
	MDSpinner:
		size_hint: None, None

		# setting up size
		size: dp(46), dp(46)

		# setting up position
		pos_hint: {'center_x': 0.5, 'center_y': 0.5}

		# active event
		active: check.active

	# designing checkbox
	MDCheckbox:
		# giving id to checkbox
		id: check

		size_hint: None, None

		# setting up position
		pos_hint: {'center_x': 0.5, 'center_y': 0.4}

		# active event
		active: True
'''


# main app class
class Main(MDApp):
    def build(self):
        # returns screen
        return Builder.load_string(KV)


# running app
Main().run()
