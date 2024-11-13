import gi
# Since a system can have multiple versions
# of GTK + installed, we want to make
# sure that we are importing GTK + 3.
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title ="GfG")

		# Create a horizontally orientated box container
		# having spacing 6 pixels
		self.box = Gtk.Box(spacing = 6)
		self.add(self.box)

		# Add a button to box container.
		# Gtk.Box.pack_start() widgets are positioned from left to right
		self.button1 = Gtk.Button(label ="Click Here")
		self.button1.connect("clicked", self.on_button1_clicked)
		self.box.pack_start(self.button1, True, True, 0)

	def on_button1_clicked(self, widget):
		print("Welcome to Geeks for Geeks.")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
