# import packages
from kivy.lang import Builder
from kivymd.app import MDApp

# writing kv lang
KV = '''
# declaring layout/screen
MDScreen:

	# this will create a space navigation bottom
	MDBottomNavigation:
		panel_color: 1,0,0,1
		text_color_active: 0, 1, 0, 1

		# this will create a navigation button on the bottom of screen
		MDBottomNavigationItem:
			name: 'screen 1'
			text: 'Camera'
			icon: 'camera'

			# this will be triggered when screen 1 is selected
			# creates a label
			MDLabel:
				text: 'You have selected Camera'
				halign: 'center'

		# this will create a navigation button on the bottom of screen
		MDBottomNavigationItem:
			name: 'screen 2'
			text: 'Microphone'
			icon: 'microphone'

			# this will be triggered when screen 2 is selected
			# creates a label
			MDLabel:
				text: 'You have selected Microphone'
				halign: 'center'

		# this will create a navigation button on the bottom of screen
		MDBottomNavigationItem:
			name: 'screen 3'
			text: 'Wi-FI'
			icon: 'wifi'

			# this will be triggered when screen 3 is selected
			# creates a label
			MDLabel:
				text: 'You have selected Wi-Fi'
				halign: 'center'
'''


# App class
class Test(MDApp):

    def build(self):
        # this will load kv lang
        screen = Builder.load_string(KV)

        # returning screen
        return screen


# running app
Test().run()
