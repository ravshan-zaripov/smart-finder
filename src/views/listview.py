from gi.repository import Adw, Gtk, Gdk, Gio, GLib, GObject # type: ignore

from src.navigator import Navigator, Entry


@Gtk.Template(resource_path="/cau/gradproject/smartfinder/ui/ListView.ui")
class ListView(Adw.NavigationPage):
    
    __gtype_name__ = "ListView"

    _gtk_list: Gtk.Box = Gtk.Template.Child()
    _back_button: Gtk.Button = Gtk.Template.Child()
    _forward_button: Gtk.Button = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

    def setup(self, app):
        self._navigator: Navigator = app.navigator

        self._back_button.connect("clicked", self.on_back_clicked)
        self._forward_button.connect("clicked", self.on_forward_clicked)

        self._navigator.connect("notify::can-go-back", self.update_navigation_buttons)
        self._navigator.connect("notify::can-go-forward", self.update_navigation_buttons)

        self.update_navigation_buttons()
        self.show_entries(self._navigator.go())

    def on_back_clicked(self, button):
        entries = self._navigator.back()
        self.show_entries(entries)

    def on_forward_clicked(self, button):
        entries = self._navigator.forward()
        self.show_entries(entries)

    def update_navigation_buttons(self, *args):
        self._back_button.set_sensitive(self._navigator.can_go_back)
        self._forward_button.set_sensitive(self._navigator.can_go_forward)

    def on_entry_clicked(self, button, entry: Entry):
        if entry.path.is_dir():
            entries = self._navigator.go(entry.path)
            self.show_entries(entries)

    def clear_box(self, box: Gtk.Box):
        child = box.get_first_child()
        while child:
            next_child = child.get_next_sibling()
            box.remove(child)
            child = next_child

    def show_entries(self, entries: list[Entry]):
        self.clear_box(self._gtk_list)

        for entry in entries:
            content = Adw.ButtonContent(label=entry.name, margin_start=5, valign=Gtk.Align.CENTER, halign=Gtk.Align.START)
            content.set_icon_name(
                "text-x-generic-symbolic" if not entry.executable else "application-x-executable-symbolic"
            )

            button = Gtk.Button(child=content, has_frame=False)
            button.connect("clicked", self.on_entry_clicked, entry)

            self._gtk_list.append(button)