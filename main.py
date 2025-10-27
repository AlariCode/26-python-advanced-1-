"""Демо модуль для курса"""

# Делаем класс Курса с ценой, названием, длительностью. Методы:
# - узнать цену
# - вывести информацию
# Делаем курс с AI и тренажёрам
# - можно расчитать рассрочку на срок курса
# Делаем курс с проектом с параметром названия проекта
# - можно расчитать рассрочку на срок курса
# - можно вывести информацию о проекте


class Course:
    def __init__(self, name: str, price: float, lenght: int):
        self.name = name
        self.price = price
        self.length = lenght

    def get_price(self):
        return self.price

    def get_info(self):
        return f"курс {self.name} по цене {self.price} длительностью {self.length}"


class AICourse(Course):
    def calculate_credit(self):
        return self.price / self.length


class ProjectCourse(Course):
    def __init__(self, name: str, price: float, lenght: int, project_name: str):
        super().__init__(name, price, lenght)
        self.project_name = project_name

    def calculate_credit(self):
        return self.price / self.length

    def get_project_info(self):
        return f"Проект: {self.project_name}"


course = ProjectCourse("Python", 10000, 2, "Калькулятор")
print(course.get_info())
print(course.get_project_info())
