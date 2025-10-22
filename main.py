"""Демо модуль для курса"""

from functools import wraps


class Limit:
    def __init__(self, count: int):
        self.count = count

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if self.count <= 0:
                raise RuntimeError("Call limit exceeded")
            self.count -= 1
            return fn(*args, **kwargs)
        return wrapper

# def limit_calls(max_calls: int):
#     def decorator(fn):
#         @wraps(fn)
#         def wrapper(self, *args, **kwargs):
#             count_arrt = f"_{fn.__name__}_count"
#             current = getattr(self, count_arrt, 0)
#             if current >= max_calls:
#                 raise RuntimeError("Call limit exceeded")
#             setattr(self, count_arrt, current + 1)
#             print(f"[LOG] {fn.__qualname__} called {current + 1}/{max_calls}")
#             return fn(self, *args, **kwargs)
#         return wrapper
#     return decorator


class Engine:
    """Двигатель"""

    @Limit(3)
    def start(self):
        """Запуск"""
        print("🚗 Двигатель запущен!")


car = Engine()

car.start()
car.start()
car.start()
car.start()  # <-- Ошибка Runtime Error
