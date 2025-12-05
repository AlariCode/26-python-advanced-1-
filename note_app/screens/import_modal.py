from textual.screen import ModalScreen
from textual.containers import Container, Horizontal
from textual.widgets import Static, Input, Button


class ImportModal(ModalScreen):
    CSS = """
        Screen {
            align: center middle;
        }

        #dialog {
            width: 60;
            height: 15;
            border: solid grey;
        }
        #title {
            dock: top;
            content-align: center middle;
            padding: 0 1;
            height: 2;
        }
        #buttons {
            align: center middle;
        }
    """

    def compose(self):
        with Container(id="dialog"):
            yield Static("Импорт данных", id="title")
            yield Input(placeholder="Введите url для импорта")
            with Horizontal(id="buttons"):
                yield Button("Импортировать", variant="primary")
                yield Button("Отмена")
