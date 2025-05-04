from gi.repository import Adw, Gtk, Gdk, Gio, GLib, GObject # type: ignore


@Gtk.Template(resource_path="/cau/gradproject/smartfinder/ui/ListView.ui")
class ListView(Adw.NavigationPage):
    
    __gtype_name__ = "ListView"

    _gtk_list: Gtk.Box = Gtk.Template.Child()
    _back_button: Gtk.Button = Gtk.Template.Child()
    _forward_button: Gtk.Button = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
