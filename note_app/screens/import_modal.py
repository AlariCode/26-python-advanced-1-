from textual.screen import ModalScreen
from textual.containers import Container, Horizontal
from textual.widgets import Static, Input, Button


class ImportModal(ModalScreen[str]):
    CSS = """
        #dialog {
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
            yield Input(placeholder="Введите url для импорта", id="input-url")
            with Horizontal(id="buttons"):
                yield Button("Импортировать", variant="primary", id="import-btn")
                yield Button("Отмена", id="cencel-btn")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "import-btn":
            url_input = self.query_one("#input-url", Input)
            url = url_input.value.strip()
            if url:
                pass
            else:
                url_input.styles.border = ("solid", "red")
        else:
            self.dismiss(None)

    async def import_data(self, url: str) -> None:
        pass
