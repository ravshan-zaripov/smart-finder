from gi.repository import Adw, Gtk, Gdk, Gio, GLib, GObject # type: ignore

from src.window import Window


class Application(Adw.Application):
    
    def __init__(self, application_id, version):
        super().__init__(application_id=application_id, version=version)

        GLib.set_application_name("SmartFinder")
        
        self._window = None

    def do_activate(self):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_resource("/cau/gradproject/smartfinder/style.css")

        Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        if not self._window:
            self._window = Window(application=self)
        self._window.present()