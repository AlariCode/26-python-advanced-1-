"""Демо модуль для курса"""


class Commands:
    def start(self): print("Старт")
    def stop(self): print("Стоп")
    def help(self): print("Помощь")


cmd = Commands()
action = input("Введите команду: ")

if hasattr(cmd, action):
    getattr(cmd, action)()
else:
    print("Команда не найдена")
