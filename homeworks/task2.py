"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто)
рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.

"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def material_costs(self):
        pass


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def material_costs(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def material_costs(self):
        return 2 * self.h + 0.3


coat = Coat(13)
suit = Suit(3)

sum_clothes = coat.material_costs + suit.material_costs

print(f"Количество материала для пальто: {coat.material_costs}")
print(f"Количество материала для костюма: {suit.material_costs}")
print(f"Общее количество материала: {sum_clothes}")
