import gi
# Since a system can have multiple versions
# of GTK + installed, we want to make
# sure that we are importing GTK + 3.
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class GridWin(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title ="GfG")

		grid = Gtk.Grid()
		self.add(grid)

		button1 = Gtk.Button(label ="Button 1")
		button2 = Gtk.Button(label ="Button 2")
		button3 = Gtk.Button(label ="Button 3")
		button4 = Gtk.Button(label ="Button 4")
		button5 = Gtk.Button(label ="Button 5")
		button6 = Gtk.Button(label ="Button 6")

		grid.add(button1)

		# With in parentheses child, left, top, width,
		# height respectively
		grid.attach(button2, 1, 0, 2, 1)

		# With in parentheses child, sibling, left, top, width,
		# height respectively
		grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
		grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 1, 1)
		grid.attach(button5, 1, 2, 1, 1)
		grid.attach_next_to(button6, button4, Gtk.PositionType.RIGHT, 1, 2)


win = GridWin()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
