"""Демо модуль для курса"""


class Positive:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, owner):
        print("Сработал get")
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        print("Сработал set")
        if value <= 0:
            raise ValueError(f"{self.name} должено быть  > 0")
        obj.__dict__[self.name] = value


class Product:
    price = Positive("price")


p = Product()
p.price = 100
print(p.price)
p.price = -1
