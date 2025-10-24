"""Демо модуль для курса"""


class Light:
    def turn_on(self):
        print("Свет включён")


class Music:
    def play(self):
        print("Музыка включена")


class SmartHome(Light, Music):
    def start(self):
        print("Умный дом активен")
        self.turn_on()
        self.play()


home = SmartHome()
home.start()
