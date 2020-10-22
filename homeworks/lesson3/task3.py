"""

Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.

"""


def my_min(custom_list):
    min_val: float = custom_list[0]
    try:
        for el in custom_list:
            if el < min_val:
                min_val = el
        return min_val
    except TypeError:
        return "TypeError"


def sum_2_max_in_3_args(*args):
    try:
        total: float = 0
        for el in args:
            total += el

        total -= my_min(args)
        return total
    except TypeError:
        return "TypeError"


print(f"Сумма двух наибольших значений = {sum_2_max_in_3_args(11, 12, 21)}")
