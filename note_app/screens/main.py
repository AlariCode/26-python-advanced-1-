from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Tree
from textual.containers import Horizontal

from note_app.widgets import MardownWidget


class MainScreen(Screen):
    CSS = """
    #tree {
        width: 25%
    }
    """

    BINDINGS = [
        ("q", "quit", "Выход")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Tree(label="Моя база знаний", id="tree")
            yield MardownWidget()
        yield Footer()

    def on_mount(self):
        self.title = "Менеджер заметок"
        self.query_one(MardownWidget).text = "## Привет"

    def action_quit(self):
        self.app.exit()
