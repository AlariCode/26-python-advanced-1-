"""Демо модуль для курса"""

# Хранилище
# Нужно реалозовать MemoryStorage и FileStorage с методами load и save
# Приложение чистает строку и передаёт в use_storage, сохарняет в одном из storage
# После успешного сохранения читает storage и выводит сохранённые данные

from typing import Protocol


class Storage(Protocol):
    """Протокол хранения"""

    def save(self, data: str) -> None: ...
    def load(self) -> str: ...


class MemoryStorage:
    """Хранение в памяти"""

    def save(self, data: str) -> None:
        self.data = data

    def load(self) -> str:
        return getattr(self, "data", "")


class FileStorage:
    """Хранение в файле"""

    def save(self, data: str) -> None:
        with open("data.txt", "w", encoding="utf-8") as f:
            f.write(data)

    def load(self) -> str:
        with open("data.txt", "r", encoding="utf-8") as f:
            return f.read()


def use_storage(storage: Storage, data: str):
    storage.save(data)
    return storage.load()


mem = MemoryStorage()
file = FileStorage()

user_input = input("Введите данные: ")
print(use_storage(mem, user_input))
print(use_storage(file, user_input))
