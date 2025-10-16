"""Демо модуль для курса"""

# Герой, у которого есть имя, hp, inventory list и пометка жив ли он
# Нужно сделать методы take_damage, heal, add_item, show_status


class Hero:
    """Герой игры"""

    def __init__(self, name: str):
        self.name = name
        self.hp = 100
        self.inventory: list[str] = []
        self.is_alive = True

    def take_damage(self, amount: int):
        """Получение урона"""
        if not self.is_alive:
            print(f"{self.name} уже повержен")
            return
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            print(f"{self.name} теперь повержен")
        else:
            print(f"{self.name} получил {amount} урона")

    def heal(self, amount):
        """Лечение"""
        if not self.is_alive:
            print(f"{self.name} уже повержен")
            return
        self.hp = min(self.hp + amount, 100)
        print(f"{self.name} восстановил {amount} HP. Текущие HP {self.hp}")

    def add_item(self, item: str):
        """Добавление предмета"""
        self.inventory.append(item)
        print(f"{self.name} получил предмет {item}")

    def show_status(self):
        """Показ статуса"""
        status = "Жив" if self.is_alive else "Повержен"
        print(
            f"{self.name} - HP: {self.hp} - Инвентарь: {self.inventory} [{status}]")


hero = Hero("Вася")
hero.add_item("Меч")
hero.show_status()
hero.take_damage(30)
hero.take_damage(60)
hero.heal(50)
hero.show_status()
