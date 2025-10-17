"""Демо модуль для курса"""


def add_repr(cls):
    """Добавление repr"""

    def __repr__(self):
        return f"{cls.__name__}[{self.__dict__}]"
    cls.__repr__ = __repr__
    return cls


@add_repr
class User:
    """Пользователь"""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


user = User("Антон", 19)
print(user)

# User = dec(User)
