"""Демо модуль для курса"""

# Управление студентами
# У нас есть студенты с именами и оценками
# Нужно сделать возможность:
# - добавить студента в список
# - получить список студентов
# - получить среднюю оценку
# - получить лучшего студента
# - распечатать отчёт - средний бал и лучший студент

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    score: int


@dataclass
class StudentRepository:
    students: list[Student]

    def add(self, student: Student):
        self.students.append(student)

    def list_all(self) -> list[Student]:
        return self.students


@dataclass
class StatisticService:
    repository: StudentRepository

    def get_avarage_score(self) -> float:
        students = self.repository.list_all()
        if not students:
            return 0
        total = sum(s.score for s in students)
        return total / len(students)

    def get_best_student(self) -> Student:
        students = self.repository.list_all()
        return max(students, key=lambda s: s.score)


@dataclass
class ReportPrinter:
    repository: StudentRepository
    stat_service: StatisticService

    def print_report(self):
        print("Отчёт по студентам")
        for s in self.repository.list_all():
            print(f"{s.name}: {s.score}")
        print(f"Средний балл: {self.stat_service.get_avarage_score()}")
        best = self.stat_service.get_best_student()
        print(f"Лучший студент: {best.name}")


repo = StudentRepository([Student("Вася", 50)])
stat_service = StatisticService(repo)
printer = ReportPrinter(repo, stat_service)
repo.add(Student("Аня", 100))
repo.add(Student("Катя", 80))

printer.print_report()
