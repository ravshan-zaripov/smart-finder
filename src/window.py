from gi.repository import Adw, Gtk, Gdk, Gio, GLib, GObject # type: ignore

from pathlib import Path

from src.widgets.sidebar import Sidebar
from src.views.listview import ListView
from src.views.searchview import SearchView


@Gtk.Template(resource_path="/cau/gradproject/smartfinder/ui/Window.ui")
class Window(Adw.ApplicationWindow):
    
    __gtype_name__ = "Window"

    _sidebar: Sidebar = Gtk.Template.Child()
    _listview: ListView = Gtk.Template.Child()

    def __init__(self, application):
        super().__init__(application=application, title="SmartFinder")

        self._app = application
        self._listview.setup(application)

        self._sidebar.connect("sidebar-folder-selected", self.on_sidebar_folder_selected)
        self._sidebar.connect("search-button-clicked", self.on_search_button_clicked)

    def on_sidebar_folder_selected(self, sidebar, path_str):
        path = Path(path_str)
        entries = self._app._navigator.go(path)
        self._listview.show_entries(entries)

    def on_search_button_clicked(self, sidebar):
        self._sidebar._search_button.set_sensitive(False) 
        dialog = SearchView()
        dialog.connect("closed", lambda d: self._sidebar._search_button.set_sensitive(True))
        dialog.present()