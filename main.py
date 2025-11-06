"""Демо модуль для курса"""

# Объекты дочерних классов должны быть взаимозаменяемы
# с объектами своих базовых классов.

# Если где-то в коде используется базовый класс,
# то можно подставить любой его наследник —
# и программа должна работать корректно, не ломаясь и не меняя поведение.

from dataclasses import dataclass


@dataclass
class User:
    name: str
    bonus: int = 0

    def add_bounus(self, amount: int):
        self.bonus += amount
        print(f"{self.name} получил {amount}. Всего {self.bonus}")


class PremiumUser(User):
    def add_bounus(self, amount: int):
        self.bonus += amount * 2
        print(f"{self.name} получил {amount}. Всего {self.bonus}")


class BannedUser(User):
    def add_bounus(self, amount: int):
        # raise Exception("Пользователь забанен")
        print(f"{self.name} не может получить бонусы")


def reward_user(user: User):
    user.add_bounus(100)


reward_user(User("Вася"))
reward_user(PremiumUser("Вася"))
reward_user(BannedUser("Вася"))
