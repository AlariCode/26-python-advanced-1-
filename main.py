"""Демо модуль для курса"""

# Заказ в интернет магазине
# Item - name, price, qty и метод subtotal() -> считает цену
# Политики скидок - NoDiscount - без скидки, PercentageDiscount - процент от заказа
# Order - list[Item] и политика скидок, метод расчёта total total_with_discount и set_policy

from dataclasses import dataclass
from typing import Protocol


class DiscountPolicy(Protocol):
    """Протокол скидок"""

    def discount(self, total: float) -> float: ...


@dataclass
class Item:
    """Единица товара"""
    name: str
    price: float
    qty: int = 1

    def subtotal(self) -> float:
        """Расчёт суммы"""
        return self.price * self.qty


class NoDiscount:
    """Политика без скидки"""

    def discount(self, total: float) -> float:
        return 0


@dataclass
class PercentageDiscount:
    """Политика с % скидки"""
    percent: float

    def discount(self, total: float) -> float:
        return total * (self.percent / 100)


@dataclass
class Order:
    """Заказ"""
    items: list[Item]
    policy: DiscountPolicy

    def total(self):
        return sum(i.subtotal() for i in self.items)

    def total_with_discount(self):
        t = self.total()
        return t - self.policy.discount(t)

    def set_policy(self, policy):
        self.policy = policy


basket = [Item("Бумага", 100, 5), Item("Ершик", 1000, 1),]
order = Order(basket, NoDiscount())
print(order.total())
print(order.total_with_discount())
order.set_policy(PercentageDiscount(10))
print(order.total())
print(order.total_with_discount())
