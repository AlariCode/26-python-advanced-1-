"""Демо модуль для курса"""


class Player:
    pass


class Light:
    def turn_on(self):
        print("Свет включён")


class Music(Player):
    def turn_on(self):
        print("Музыка включена")


class SmartHome(Music, Light):
    def play(self):
        print("Альтернативный play")

    def start(self):
        print("Умный дом активен")
        self.turn_on()


home = SmartHome()
home.start()
print(SmartHome.mro())
