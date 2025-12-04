from pathlib import Path
from note_app.domain import Note
from note_app.repositories.base_note_repository import BaseNoteRepository


class NoteRepository(BaseNoteRepository):

    def __init__(self, base_path: Path) -> None:
        self.base_path = base_path.resolve()

    def _check_path(self, path: Path):
        """Проверка пути"""
        if not path.exists() or not path.is_dir():
            raise ValueError(f"Note doen't exist: {path}")

        if self.base_path not in path.parents and path != self.base_path:
            raise ValueError("Access outside data directory in not allowed")

    def get_notes_by_path(self, path: Path) -> list[Note]:
        """Получение заметок"""
        path = path.resolve()
        self._check_path(path)

        notes: list[Note] = []

        for sub_path in path.iterdir():
            if sub_path.is_file() and not sub_path.name.startswith(".") and sub_path.suffix == ".md":
                notes.append(
                    Note(
                        name=sub_path.name,
                        path=sub_path
                    )
                )
        return sorted(notes, key=lambda f: f.name)

    def create_note(self, path: Path, name: str) -> Note:
        """Создание директории"""
        self._check_path(path)

        if not name or "/" in name or "\\" in name:
            raise ValueError("Invalid note name")

        path.mkdir(parents=True, exist_ok=False)
        return Note(name, path)

    def delete_note(self, note: Note) -> None:
        """Удаление директории"""
        path = note.path.resolve()
        self._check_path(path)
        path.unlink()
