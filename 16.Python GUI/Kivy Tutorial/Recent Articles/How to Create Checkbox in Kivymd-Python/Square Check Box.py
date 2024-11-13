# importing builder
from kivy.lang import Builder

# importing MDApp
from kivymd.app import MDApp

# writing kv lang
KV = '''
# defining layout
MDFloatLayout:
	# this will create check Box
	MDCheckbox:

		# defining size to check box
		size: "48dp", "48dp"
		size_hint: None,None

		# giving location
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
