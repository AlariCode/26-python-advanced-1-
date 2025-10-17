"""Демо модуль для курса"""


def log_decorator(func):
    def wrapper():
        print("Функция началась")
        func()
        print("Функция завершилась")
    return wrapper


@log_decorator
def say_hello():
    print("Привет!")


say_hello()
