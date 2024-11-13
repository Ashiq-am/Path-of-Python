# importing packages
from kivy.lang import Builder
from kivymd.app import MDApp

# writing kv lang
KV = '''
# declaring screen
MDScreen:

	# desiging MDSpinner
	MDSpinner:
		size_hint: None, None

		# sets length and width of spinner to 46dp
		size: dp(46), dp(46)

		# sets position of spinner on screen
		pos_hint: {'center_x': 0.5, 'center_y': 0.5}

		active: True

'''


# main app class
class Main(MDApp):
    def build(self):
        # returns kv
        return Builder.load_string(KV)


# running app
Main().run()
