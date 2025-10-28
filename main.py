"""Демо модуль для курса"""

len("Purple")
len([1, 2, 3])
len({1: "a", 2: "b"})


class Payment:
    def pay(self, amount):
        raise NotImplementedError("Метод должен быть определён")


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Оплата картой: {amount}")


class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"Оплата криптой: {amount}")


class ApplePayment(Payment):
    def pay(self, amount):
        print(f"Оплата apple: {amount}")


payments = [CardPayment(), CryptoPayment(), ApplePayment()]
for p in payments:
    p.pay(100)
