import gi
# Since a system can have multiple versions
# of GTK + installed, we want to make
# sure that we are importing GTK + 3.
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title ="Geeks for Geeks")
		self.set_border_width(70)

		# Create Notebook
		self.notebook = Gtk.Notebook()
		self.add(self.notebook)

		# Create Boxes
		self.page1 = Gtk.Box()
		self.page1.set_border_width(50)
		self.page1.add(Gtk.Label("Welcome to Geeks for Geeks"))
		self.notebook.append_page(self.page1, Gtk.Label("Click Here"))

		self.page2 = Gtk.Box()
		self.page2.set_border_width(50)
		self.page2.add(Gtk.Label("A computer science portal for geeks"))
		self.notebook.append_page(self.page2, Gtk.Label("Click Here"))


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
# Display the window.
win.show_all()
# Start the GTK + processing loop
Gtk.main()
