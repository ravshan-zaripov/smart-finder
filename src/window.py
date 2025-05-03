from gi.repository import Adw, Gtk, Gdk, Gio, GLib, GObject # type: ignore

from src.widgets.sidebar import Sidebar


@Gtk.Template(resource_path="/cau/gradproject/smartfinder/ui/Window.ui")
class Window(Adw.ApplicationWindow):
    
    __gtype_name__ = "Window"

    _sidebar: Sidebar = Gtk.Template.Child()

    def __init__(self, application):
        super().__init__(application=application, title="SmartFinder")
