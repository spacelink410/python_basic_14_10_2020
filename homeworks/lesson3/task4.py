"""

Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

"""


def my_func(numb, power):
    return numb**power


def my_func2(numb, power):
    i: int = power
    numb: float = 1 / numb
    while i < -1:
        numb *= numb
        i += 1
    return numb


x: float = 0.0
y: float = 0.0

try:
    x = float(input("Введите положительное действительное число: "))
    y = int(input("Введите целое отрицательное число: "))
    if y == 0:
        print("Y не может быть равен 0")
    elif x < 0:
        print("X Должен быть положительным числом")
    elif y > 0:
        print("Y Должен быть отрицательным числом")
    else:
        print(my_func(x, y))
        print(my_func2(x, y))
except ValueError:
    print("Введено неверное значение")
