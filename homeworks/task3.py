"""Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name,
surname,
position (должность),
income (доход).

Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад,
премия.

Например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

"""


class Worker:
    name: str = 'Alan'
    surname: str = 'Turing'
    position: str = 'Programmer'
    inheritors: list = []
    _income: dict = {'wage': 1000, 'bonus': 5000}


class Position(Worker):
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
        self.inheritors.append(self)

    def get_full_name(self):
        return self.name + ' ' + self.surname + ' '

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker = Worker()
employee1 = Position('Ivan', 'Ivanov', 'Manager', {'wage': 20000, 'bonus': 100000})
employee2 = Position('Petr', 'Petrov', 'Programmer', {'wage': 100000, 'bonus': 0})
employee3 = Position('Sidr', 'Sidorov', 'Manager', {'wage': 15000, 'bonus': 50000})

for el in worker.inheritors:
    print('\nКласс наследник')
    for attribute in dir(el):
        if attribute[0] != '_' and not callable(getattr(el, attribute)):
            print('Атрибут класса насследика', attribute, ':', getattr(el, attribute))

print('\nБазовый класс')
for attribute in dir(worker):
    if attribute[0] != '_' and not callable(getattr(worker, attribute)):
        print('Атрибут базового класса', attribute, ':', getattr(worker, attribute))

print('\nПолное имя: ' + employee1.get_full_name())
print('Доход: ' + str(employee1.get_total_income()))

print('\nПолное имя: ' + employee2.get_full_name())
print('Доход: ' + str(employee2.get_total_income()))

print('\nПолное имя: ' + employee3.get_full_name())
print('Доход: ' + str(employee3.get_total_income()))
