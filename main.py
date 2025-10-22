"""Демо модуль для курса"""


def log_call(fn):
    """Логирует вызов"""
    def wrapper(*args, **kwargs):
        print(f"[LOG] {fn.__qualname__} args={args} kwargs={kwargs}")
        return fn(*args, **kwargs)
    return wrapper


class Service:
    """Сервисный"""

    @log_call
    def process(self, x: float) -> float:
        return x * 2


s = Service()
s.process(10)
