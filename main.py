"""Демо модуль для курса"""


class User:
    def __init__(self, name: str, balance: float) -> None:
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Сумма должна быть положительной")

    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Недостаточно средств")


u = User("Антон", 1000)
u.deposit(500)
print(u.get_balance())
u.withdraw(700)
print(u.get_balance())
print(u.__dict__)
print(u.get_balance())
