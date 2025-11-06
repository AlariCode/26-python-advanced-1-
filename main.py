"""Демо модуль для курса"""

# Создать 3 метода платежи:
# - Всё сумму
# - Всё сумму - число бонусов
# - Деление на N частей, 1 сразу, остальные потом


from dataclasses import dataclass


class Payment:
    def pay(self, amount: float) -> float:
        """Метод, который возвращает текущую сумму для списания"""
        print(f"Списано: {amount}")
        return amount


@dataclass
class BonusPayment(Payment):
    bonuses: float

    def pay(self, amount: float) -> float:
        final = amount - self.bonuses
        print(f"Списано: {final}")
        return final


@dataclass
class InstallmentPayment(Payment):
    part: int

    def pay(self, amount: float) -> float:
        final = amount / self.part
        print(f"Списано: {final}")
        return final


def pay(method: Payment):
    return method.pay(100)


pay(InstallmentPayment(2))
