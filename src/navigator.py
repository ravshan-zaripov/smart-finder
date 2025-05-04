from gi.repository import GObject # type: ignore

import os
from pathlib import Path


class Entry:
    
    def __init__(self, name: str, path: Path, ext: str, exec: bool):
        self.name = name
        self.path = path
        self.extension = ext
        self.executable = exec


class Navigator(GObject.GObject):

    def __init__(self):
        super().__init__()

        self.history_stack = []
        self.forward_stack = []
        self.home_path = Path.home()

    def go(self, path=None):
        current_path = Path(path) if path else self.home_path

        if not current_path.is_dir():
            raise ValueError(f"Invalid directory: {current_path}")

        if not self.history_stack or self.history_stack[-1] != current_path:
            self.history_stack.append(current_path)
            self.forward_stack.clear()

        self.notify("can-go-back")
        self.notify("can-go-forward")
        return self._list_entries(current_path)

    @GObject.Property(type=bool, default=False, flags=GObject.ParamFlags.READABLE)
    def can_go_back(self):
        return len(self.history_stack) > 1

    @GObject.Property(type=bool, default=False, flags=GObject.ParamFlags.READABLE)
    def can_go_forward(self):
        return len(self.forward_stack) > 0

    def back(self):
        if len(self.history_stack) > 1:
            path = self.history_stack.pop()
            self.forward_stack.append(path)

            self.notify("can-go-back")
            self.notify("can-go-forward")
            return self._list_entries(self.history_stack[-1])
        return []

    def forward(self):
        if len(self.forward_stack) > 0:
            path = self.forward_stack.pop()
            self.history_stack.append(path)

            self.notify("can-go-back")
            self.notify("can-go-forward")
            return self._list_entries(path)
        return []

    def _list_entries(self, path: Path):
        return [
            Entry(
                name=entry.name,
                path=Path(entry.path),
                ext=Path(entry.path).suffix if entry.is_file() else "",
                exec=os.access(entry.path, os.X_OK),
            )
            for entry in os.scandir(path)
        ]
