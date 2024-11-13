import gi

# Since a system can have multiple versions
# of GTK + installed, we want to make
# sure that we are importing GTK + 3.
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

# Creates an empty window.
window = Gtk.Window()

# Connecting to the window’s delete event
# to ensure that the application is terminated
# whenever we click close button

window.connect("destroy", Gtk.main_quit)
# Display the window.
window.show_all()

Gtk.main()
