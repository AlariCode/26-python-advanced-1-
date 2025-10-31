"""Демо модуль для курса"""

# Принцип открытости и закрытости
# Классы должны быть открыты для расширения, но закрыты для модификации.


# class DiscountCalculator:
#     def calculate(self, user_type: str, amount: float) -> float:
#         if user_type == "student":
#             return amount * 0.9
#         elif user_type == "vip":
#             return amount * 0.8
#         else:
#             return amount


from abc import ABC, abstractmethod
from dataclasses import dataclass


class DiscountPolicy(ABC):
    @abstractmethod
    def apply_discount(self, amount: float) -> float:
        pass


class NoDiscount(DiscountPolicy):
    def apply_discount(self, amount: float) -> float:
        return amount


class StudentDiscount(DiscountPolicy):
    def apply_discount(self, amount: float) -> float:
        return amount * 0.9


class VipDiscount(DiscountPolicy):
    def apply_discount(self, amount: float) -> float:
        return amount * 0.8


class GuestDiscount(DiscountPolicy):
    def apply_discount(self, amount: float) -> float:
        return amount * 0.95


@dataclass
class DiscountCalculator:
    policy: DiscountPolicy

    def calculate(self, amount: float) -> float:
        return self.policy.apply_discount(amount)


calc = DiscountCalculator(GuestDiscount())
print(calc.calculate(1000))
