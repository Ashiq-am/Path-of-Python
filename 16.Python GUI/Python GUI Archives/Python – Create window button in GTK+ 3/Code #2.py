import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Define our own newWindow class.
class newWindow(Gtk.Window):
	def __init__(self):

		# Call the constructor of the super class.
		# Set the value of the property title to Geeks for Geeks.
		Gtk.Window.__init__(self, title ="Geeks for Geeks")

		# Create a button widget, connect to its clicked signal
		# and add it as child to the top-level window.
		self.button = Gtk.Button(label ="Click Here")
		self.button.connect("clicked", self.on_button_clicked)
		self.add(self.button)

	# When we click on the button this method
	# will be called
	def on_button_clicked(self, widget):
		print("Geeks for Geeks")


win = newWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
