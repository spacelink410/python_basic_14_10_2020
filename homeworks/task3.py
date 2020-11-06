"""Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).

В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()),
вычитание (__sub__()),
умножение (__mul__()),
деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно.

В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных
двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух
клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида
*****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
 *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.

"""

import random


class Nucleus:
    cell: int

    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        new_nucleus = Nucleus(self.cell + other.cell)
        return new_nucleus

    def __sub__(self, other):
        new_nucleus = Nucleus(self.cell - other.cell)
        return new_nucleus

    def __mul__(self, other):
        new_nucleus = Nucleus(self.cell * other.cell)
        return new_nucleus

    def __truediv__(self, other):
        """Округлим по всем правилам математики. Аналогично, если клетка имеет больше половины
        ресурсов, то она выживет. Если у нее осталось менее половины, то она умрет

        """
        new_nucleus = Nucleus(round(self.cell / other.cell))
        return new_nucleus

    def make_order(self, item_in_row):
        matrix_size = divmod(self.cell, item_in_row)
        nuc_str = ""

        for el in range(matrix_size[0]):
            nuc_str += "*" * item_in_row + "\n"

        nuc_str += "*" * matrix_size[1]

        return nuc_str


class Container:
    nucleus_list: list = []

    def append_nuc(self, cell):
        self.nucleus_list.append(Nucleus(cell))

    def add_nuc(self):
        if len(self.nucleus_list) > 1:
            nuc_1: Nucleus = self.nucleus_list.pop(random.randint(0, len(self.nucleus_list)) - 1)
            nuc_2: Nucleus = self.nucleus_list.pop(random.randint(0, len(self.nucleus_list)) - 1)
            print(f"\nОперация сложения\nВзята клетка с ячейками: {nuc_1.cell} и с ячейками: {nuc_2.cell}")
            self.nucleus_list.append(nuc_1 + nuc_2)
            print(f"Новая клетка c ячейками: {self.nucleus_list[-1].cell}")
        else:
            print(f"\nНевозможно сложить клетки")

    def sub_nuc(self):
        if len(self.nucleus_list) > 1:
            nuc_1: Nucleus = self.nucleus_list.pop(random.randint(0, len(self.nucleus_list)) - 1)
            nuc_2: Nucleus = self.nucleus_list.pop(random.randint(0, len(self.nucleus_list)) - 1)
            print(f"\nОперация вычитания\nВзята клетка с ячейками: {nuc_1.cell} и с ячейками: {nuc_2.cell}")
            if nuc_1.cell > nuc_2.cell:
                self.nucleus_list.append(nuc_1 - nuc_2)
            else:
                self.nucleus_list.append(nuc_2 - nuc_1)
            print(f"Новая клетка c ячейками: {self.nucleus_list[-1].cell}")
        else:
            print("Невозможно вычесть клетки")

    def mul_nuc(self):
        if len(self.nucleus_list) > 1:
            nuc_1: Nucleus = self.nucleus_list.pop(random.randint(0, len(self.nucleus_list)) - 1)
            nuc_2: Nucleus = self.nucleus_list.pop(random.randint(0, len(self.nucleus_list)) - 1)
            print(f"\nОперация умножения\nВзята клетка с ячейками: {nuc_1.cell} и с ячейками: {nuc_2.cell}")
            self.nucleus_list.append(nuc_1 * nuc_2)
            print(f"Новая клетка c ячейками: {self.nucleus_list[-1].cell}")
        else:
            print("\nНевозможно умножить клетки")

    def div_nuc(self):
        """Изменил функцию деления. Провел аналогию столкнвения клеток:
        слабая - сильная
        сильная - слабая
        мертвая - обычная
        обычная - мертвая
        мертвая - мертвая

        мертвые клетки в результате операции выкидываются из контейнера

        """

        if len(self.nucleus_list) > 1:
            nuc_1: Nucleus = self.nucleus_list.pop(random.randint(0, len(self.nucleus_list)) - 1)
            nuc_2: Nucleus = self.nucleus_list.pop(random.randint(0, len(self.nucleus_list)) - 1)

            if nuc_1.cell == 0 and nuc_2.cell != 0:
                print(f"\nОперация деления\nВзята клетка с ячейками: {nuc_1.cell} и с ячейками: {nuc_2.cell}")
                self.nucleus_list.append(nuc_2)
                print(f"Клетка с ячейками: {nuc_1.cell} мертвая. "
                      f"Клетка с ячейками {self.nucleus_list[-1].cell} вернулась обратно")

            if nuc_1.cell != 0 and nuc_2.cell == 0:
                print(f"\nОперация деления\nВзята клетка с ячейками: {nuc_1.cell} и с ячейками: {nuc_2.cell}")
                self.nucleus_list.append(nuc_1)
                print(f"Клетка с ячейками: {nuc_2.cell} мертвая. "
                      f"Клетка с ячейками {self.nucleus_list[-1].cell} вернулась обратно")

            if nuc_1.cell != 0 and nuc_2.cell != 0:
                print(f"\nОперация деления\nВзята клетка с ячейками: {nuc_1.cell} и с ячейками: {nuc_2.cell}")
                self.nucleus_list.append(nuc_1 / nuc_2)
                print(f"Новая клетка c ячейками: {self.nucleus_list[-1].cell}")

            if nuc_1 == 0 and nuc_2 == 0:
                print("Обе клетки мертвы")
        else:
            print("\nНевозможно разделить клетки")

    def get_nuc(self, row, numb):
        """Функция возвращает визуальную модель клетки в зависимости от количества ячеек внутри нее

        :param row: количество ячеек в ряду
        :param numb: номер клетки в контейнере
        :return: строка с визуальной моделью клетки

        """
        if numb - 1 < len(self.nucleus_list):
            print(self.nucleus_list[numb - 1].make_order(row))
        else:
            print("Нет клетки по текущему индексу")


c = Container()
c.append_nuc(23)
c.append_nuc(5)
c.append_nuc(6)
c.append_nuc(90)

# Протестируем, как все клетки сойдутся к 1 большой
c.add_nuc()
c.add_nuc()
c.add_nuc()
c.add_nuc()

# Протестируем, как все клетки сойдутся к 1 маленькой или умрут
# c.sub_nuc()
# c.sub_nuc()
# c.sub_nuc()
# c.sub_nuc()

# Протестируем, как все клетки сойдутся к 1 огромной
# c.mul_nuc()
# c.mul_nuc()
# c.mul_nuc()
# c.mul_nuc()

# Протестируем, как все клетки сойдутся к 1 ммаленькой или умрут
# c.div_nuc()
# c.div_nuc()
# c.div_nuc()
# c.div_nuc()

c.get_nuc(58, 1)
