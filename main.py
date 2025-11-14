# Нужно сделать Repository, который работает с любымим типами и имеет методы:
# add - добавляет в список элемент
# get_by_index - получает по index
# get_all - получает все

# Всё хранится как  list

from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar("T")


@dataclass
class Repository(Generic[T]):
    items: list[T]

    def add(self, item: T):
        self.items.append(item)

    def det_by_index(self, index: int) -> Optional[T]:
        if 0 <= index < len(self.items):
            return self.items[index]
        return None

    def get_all(self) -> list[T]:
        return self.items


repo = Repository[str](["a", "b"])
print(repo.det_by_index(2))
