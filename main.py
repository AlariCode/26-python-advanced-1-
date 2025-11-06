"""Демо модуль для курса"""

# DIP

# Модули верхних уровней не должны зависеть от модулей нижних уровней.

# Оба типа модулей должны зависеть от абстракций.

# Абстракции не должны зависеть от деталей.

# Детали должны зависеть от абстракций.

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Logger(ABC):
    @abstractmethod
    def log(self, message: str): ...


class FileLogger(Logger):
    def log(self, message: str):
        print(f"Запись в файл: {message}")


class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"Запись в консоль: {message}")


@dataclass
class UserService:
    logger: Logger

    def create_user(self, name: str):
        # Создаёт пользователя
        self.logger.log(f"Создан аккаунт {name}")


service = UserService(ConsoleLogger())
