"""Демо модуль для курса"""

# Single Responsibility Principle (SRP)
# Класс должен иметь только одну причину для изменения.

from dataclasses import dataclass


@dataclass
class Order:
    items: list[str]

    def calculate_total(self):
        return len(self.items) * 10


class OrderRepository:
    def save_to_db(self, order: Order):
        print("Сохранение в базу")


class EmailService:
    def send_confirmation_email(self, email: str, order: Order):
        print("Отправка письма")
