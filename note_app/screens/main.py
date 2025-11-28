from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Tree, Markdown
from textual.containers import Horizontal


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
            yield Markdown("# Привет! Я загловок")
        yield Footer()

    def on_mount(self):
        self.title = "Менеджер заметок"

    def action_quit(self):
        self.app.exit()
