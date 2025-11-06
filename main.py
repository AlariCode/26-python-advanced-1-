"""Демо модуль для курса"""

# Клиенты не должны зависеть от методов, которые они не используют.
# Не заставляй классы реализовывать методы, которые им не нужны.


# class PaymentProcessor:
#     def pay(self, amount: float):
#         pass

#     def refund(self, amount: float):
#         pass

#     def tokenize_card(self, card_number: str):
#         pass

#     def check_balance(self):
#         pass

from abc import ABC, abstractmethod


class Payable(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

    @abstractmethod
    def refund(self, amount: float):
        pass


class Tokenazable(ABC):
    @abstractmethod
    def tokenize_card(self, card_number: str):
        pass


class BalanceCheckable(ABC):
    @abstractmethod
    def check_balance(self):
        pass


class Card(Payable, Tokenazable):
    def pay(self, amount: float):
        pass

    def refund(self, amount: float):
        pass

    def tokenize_card(self, card_number: str):
        pass


class Paypal(Payable, BalanceCheckable):
    def pay(self, amount: float):
        pass

    def refund(self, amount: float):
        pass

    def check_balance(self):
        pass
