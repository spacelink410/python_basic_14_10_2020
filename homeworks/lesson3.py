"""Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.

"""
from homeworks import my_func as mf

new_list: list = list((el for el in mf.my_range(20, 240) if el % 20 == 0 or el % 21 == 0))
print(new_list)
