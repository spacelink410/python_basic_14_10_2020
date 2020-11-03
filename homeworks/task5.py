"""Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""


class Stationery:
    title: str = 'Что-то рисующее'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки - {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки - {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки - {self.title}')


st = Stationery()
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

st.draw()
pen.draw()
pencil.draw()
handle.draw()
