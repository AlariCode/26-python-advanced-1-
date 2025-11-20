# Есть User, Product и Order у которых есть поле id.
# Нужно сделать универвальную функицю поиска по id

from dataclasses import dataclass
from typing import Optional, Protocol, TypeVar


class Identifieble(Protocol):
    id: int


T = TypeVar("T", bound=Identifieble)


@dataclass
class User:
    id: int
    email: str


@dataclass
class Product:
    id: int
    title: str


@dataclass
class Order:
    id: int
    producs: list[Product]


def get_by_id(items: list[T], id_: int) -> Optional[T]:
    for item in items:
        if item.id == id_:
            return item
    return None


get_by_id([User(1, "a@a.ru")], 1)
