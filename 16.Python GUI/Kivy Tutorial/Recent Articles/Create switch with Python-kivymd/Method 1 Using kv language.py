# importing packages
from kivy.lang import Builder
from kivymd.app import MDApp

# writing kv lang
KV = '''

# declaring layout
MDFloatLayout:

	# this will create a switch
	MDSwitch:
		# giving position to the switch on screen
		pos_hint: {'center_x': .5, 'center_y': .5}
'''


# app class
class Test(MDApp):
    def build(self):
        # this will load kv lang
        screen = Builder.load_string(KV)

        # returning screen
        return screen


# running app
Test().run()
