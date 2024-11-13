# importing packages
from kivy.lang import Builder
from kivy.factory import Factory
from kivymd.app import MDApp

# it will load the kv
# Note: we need not to import MDBanner
# or anything if working with kv
Builder.load_string('''
<Banner@Screen>
	# this will create a banner
	MDBanner:
		id: banner
		text: ["GEEKS FOR GEEKS."]

		# defining button in banner
		left_action: ["LEARN MORE", lambda x: None]
		right_action: ["CLOSE", lambda x: None]

		# defining size to banner
		over_widget: screen
		vertical_pad: toolbar.height

	# this will create a toolbar
	MDToolbar:
		id: toolbar
		title: "Example Banners"
		elevation: 10
		pos_hint: {'top': 1}

	# this will create a vertical box layout
	MDBoxLayout:
		id: screen
		orientation: "vertical"
		size_hint_y: None
		height: Window.height - toolbar.height

		# it will trigger banner to show
		OneLineListItem:
			text: "CLICK HERE"
			on_release: banner.show()

		#we don't need widgets so we will leave widget empty
		#or you can simply remove it
		Widget:
''')


# App class
class Test(MDApp):
    def build(self):
        # Factory.banner is our kv lang we wrote
        # which was loader by builder.load_string()
        # and stored in Factory
        return Factory.Banner()


# running app
Test().run()
