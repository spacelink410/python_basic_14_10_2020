"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего
дорожного полотна. Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
* число см толщины полотна.
Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т

"""


class Road:
    _length: int = 0
    _width: int = 0
    _mass: int = 0
    _thickness: int = 0

    def __init__(self, length, width, mass, thickness):
        self._length = length
        self._width = width
        self._mass = mass
        self._thickness = thickness

    def total_mass(self):
        return self._length * self._width * self._thickness * self._mass


r = Road(20, 5000, 25, 5)
try:
    print(f'Общая масса асфальта {r.total_mass() / 1000} т.')
except TypeError:
    print('Неверный формат данных')
