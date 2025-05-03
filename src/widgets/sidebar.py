from gi.repository import Adw, Gtk, Gdk, Gio, GLib, GObject # type: ignore


@Gtk.Template(resource_path="/cau/gradproject/smartfinder/ui/Sidebar.ui")
class Sidebar(Adw.NavigationPage):
    
    __gtype_name__ = "Sidebar"

    _search_button: Gtk.Button = Gtk.Template.Child()
    _menu_button: Gtk.Button = Gtk.Template.Child()
    _gtk_list: Gtk.Box = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

        self.add_folder("Home", "user-home-symbolic")
        self.add_folder("Documents", "folder-documents-symbolic")
        self.add_folder("Downloads", "folder-download-symbolic")
        self.add_folder("Videos", "folder-videos-symbolic")
        self.add_folder("Music", "folder-music-symbolic")
        self.add_folder("Pictures", "folder-pictures-symbolic")

    def add_folder(self, label, icon):
        content = Adw.ButtonContent(label=label, icon_name=icon, margin_start=5, valign=Gtk.Align.CENTER, halign=Gtk.Align.START)

        button = Gtk.Button(child=content, has_frame=False)

        self._gtk_list.append(button)
