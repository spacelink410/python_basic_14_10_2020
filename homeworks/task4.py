"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed,
color,
name,
is_police (булево).

А также методы:
go,
stop,
turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

"""


class Car:
    speed: float
    color: str
    name: str
    is_police: bool
    collection: list = []

    def car_go(self):
        print(f'{self.name} поехала')

    def car_stop(self):
        print(f'{self.name} остановилась')

    def car_turn(self, direction: int):
        if direction:
            print(f'{self.name} повернула направо')
        else:
            print(f'{self.name} повернула налево')

    def show_speed(self):
        print(f'Скорость {self.name} = {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.collection.append(self)

    def show_speed(self):
        print(f'{self.name} превысила скорость 60 км/ч') \
            if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.collection.append(self)

    def show_speed(self):
        print(f'{self.name} превысила скорость 40 км/ч') \
            if self.speed > 40 else super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.collection.append(self)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.collection.append(self)


ex_car = Car()
t_car = TownCar(70, 'green', 'Toyota', False)
s_car = SportCar(180, 'black', 'Agera RS', False)
w_car = WorkCar(40, 'white', 'Daewoo', False)
p_car = PoliceCar(220, 'multicolored', 'BMW', True)

for el in ex_car.collection:
    print('\nКласс наследник')
    for attribute in dir(el):
        if attribute[0] != '_' and not callable(getattr(el, attribute)):
            print(attribute, ':', getattr(el, attribute))

    print(f'\nВызовы методов {el.name}')
    el.car_go()
    el.car_stop()
    el.car_turn(1)
    el.car_turn(0)
    el.show_speed()
    print('\n======================================')
