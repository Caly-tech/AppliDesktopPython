import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonPressed(self, button):
        print("Hello World!")


builder = Gtk.Builder()
builder.add_from_file("main_page.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainWindow")
window.show_all()

Gtk.main()