# writing kv lang
KV = '''
# declaring layout/screen
MDScreen:

	# this will create a space navigation bottom
	MDBottomNavigation:

		# this will create a navigation button on the bottom of screen
		MDBottomNavigationItem:
			name: 'screen 1'
			text: 'Python'
			icon: 'language-python'

			# this will be triggered when screen 1 is selected
			# creates a label
			MDLabel:
				text: 'Python'
				halign: 'center'

		# this will create a navigation button on the bottom of screen
		MDBottomNavigationItem:
			name: 'screen 2'
			text: 'Java'
			icon: 'language-java'

			# this will be triggered when screen 2 is selected
			# creates a label
			MDLabel:
				text: 'Java'
				halign: 'center'

		# this will create a navigation button on the bottom of screen
		MDBottomNavigationItem:
			name: 'screen 3'
			text: 'CPP'
			icon: 'language-cpp'

			# this will be triggered when screen 3 is selected
			# creates a label
			MDLabel:
				text: 'CPP'
				halign: 'center'
'''
