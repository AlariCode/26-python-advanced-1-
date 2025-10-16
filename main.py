"""Демо модуль для курса"""


class Note:
    """Заметка"""

    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description


note = Note("Заметка", "Это моя заметка")
print(note.description)
note_next = Note("Моя заметка")
