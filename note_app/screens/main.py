from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer
from textual.containers import Horizontal

from note_app.config.config import AppSettings
from note_app.repositories import FolderRepository
from note_app.repositories.note_repository import NoteRepository
from note_app.widgets import NoteViewWidget
from note_app.widgets.file_tree import FileTreeWidget


class MainScreen(Screen):
    CSS = """
    #tree {
        width: 25%
    }
    """

    BINDINGS = [
        ("q", "quit", "Выход")
    ]

    def __init__(self, settings: AppSettings, *args, **kwargs) -> None:
        self.settings = settings
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        folder_repo = FolderRepository(self.settings.data_directory)
        note_repo = NoteRepository(self.settings.data_directory)
        yield Header()
        with Horizontal():
            yield FileTreeWidget(folder_repo, note_repo)
            yield NoteViewWidget()
        yield Footer()

    def on_mount(self):
        self.title = "Менеджер заметок"
        self.query_one(NoteViewWidget).text = "## Привет"

    def action_quit(self):
        self.app.exit()

    def on_file_tree_widget_note_selected(self, message: FileTreeWidget.NoteSelected) -> None:
        self.notify(message.note_path._str)
