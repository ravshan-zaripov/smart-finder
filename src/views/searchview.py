from gi.repository import Adw, Gtk, Gdk, Gio, GLib, GObject # type: ignore


@Gtk.Template(resource_path="/cau/gradproject/smartfinder/ui/SearchView.ui")
class SearchView(Adw.Dialog):

    __gtype_name__ = "SearchView"

    _search_entry: Gtk.SearchEntry = Gtk.Template.Child()
    _gtk_list: Gtk.Box = Gtk.Template.Child()

    def __init__(self):
        super().__init__()