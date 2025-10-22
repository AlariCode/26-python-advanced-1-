"""Демо модуль для курса"""

import random


def retry(times: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attemp in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Попытка {attemp} не удалась: {e}")
                    if attemp == times:
                        print("Все попытки завершены")
        return wrapper
    return decorator


@retry(3)
def unstable():
    """Иногда падает с ошибкой"""
    if random.random() < 0.7:
        raise ValueError("Ошибка соединения")
    print("✅ Успешное выполнение")


unstable()
