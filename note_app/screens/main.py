from typing import Optional
import html2text
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer
from textual.containers import Horizontal

from note_app.config.config import AppSettings
from note_app.repositories import BaseFolderRepository, BaseNoteRepository
from note_app.screens.import_modal import ImportModal
from note_app.widgets import NoteViewWidget
from note_app.widgets.file_tree import FileTreeWidget


class MainScreen(Screen):
    CSS = """
    #tree {
        width: 25%
    }
    """

    BINDINGS = [
        ("q", "quit", "Выход"),
        ("i", "import", "Импорт"),
    ]

    def __init__(self, settings: AppSettings, folder_repo: BaseFolderRepository, note_repo: BaseNoteRepository, * args, **kwargs) -> None:
        self.settings = settings
        self._folder_repo = folder_repo
        self._note_repo = note_repo
        self._dir = settings.data_directory
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield FileTreeWidget(self._folder_repo, self._note_repo)
            yield NoteViewWidget()
        yield Footer()

    def on_mount(self):
        self.title = "Менеджер заметок"

    def action_import(self):
        self.app.push_screen(ImportModal(), self.handle_import)

    def action_quit(self):
        self.app.exit()

    def handle_import(self, data: Optional[str]):
        if data:
            md = html2text.html2text(data)
            self._note_repo.create_note(self._dir, "imported", md)

    def on_file_tree_widget_note_selected(self, message: FileTreeWidget.NoteSelected) -> None:
        note = self._note_repo.load_note(message.note_path)
        if note.content:
            self.query_one(NoteViewWidget).text = note.content
        else:
            self.query_one(NoteViewWidget).text = ""

    def on_file_tree_widget_folder_selected(self, message: FileTreeWidget.FolderSelected) -> None:
        self._dir = message.folder_path
