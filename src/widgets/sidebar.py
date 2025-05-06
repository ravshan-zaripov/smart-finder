from gi.repository import Adw, Gtk, Gdk, Gio, GLib, GObject # type: ignore

from pathlib import Path


@Gtk.Template(resource_path="/cau/gradproject/smartfinder/ui/Sidebar.ui")
class Sidebar(Adw.NavigationPage):
    
    __gtype_name__ = "Sidebar"

    __gsignals__ = {
        "sidebar-folder-selected": (GObject.SignalFlags.RUN_FIRST, None, (str,)),
        "search-button-clicked": (GObject.SignalFlags.RUN_FIRST, None, ()),
    }

    _search_button: Gtk.Button = Gtk.Template.Child()
    _menu_button: Gtk.Button = Gtk.Template.Child()
    _gtk_list: Gtk.Box = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

        self.add_folder("Home", "user-home-symbolic", Path.home())
        self.add_folder("Documents", "folder-documents-symbolic", Path.home() / "Documents")
        self.add_folder("Downloads", "folder-download-symbolic", Path.home() / "Downloads")
        self.add_folder("Videos", "folder-videos-symbolic", Path.home() / "Videos")
        self.add_folder("Music", "folder-music-symbolic", Path.home() / "Music")
        self.add_folder("Pictures", "folder-pictures-symbolic", Path.home() / "Pictures")

        self._search_button.connect("clicked", self.on_search_button_clicked)

    def add_folder(self, label: str, icon: str, path: Path):
        content = Adw.ButtonContent(
            label=label,
            icon_name=icon,
            margin_start=5,
            valign=Gtk.Align.CENTER,
            halign=Gtk.Align.START
        )
        button = Gtk.Button(child=content, has_frame=False)
        button.connect("clicked", self.on_folder_clicked, path)
        self._gtk_list.append(button)

    def on_folder_clicked(self, button, path: Path):
        self.emit("sidebar-folder-selected", str(path))

    def on_search_button_clicked(self, button):
        self.emit("search-button-clicked")