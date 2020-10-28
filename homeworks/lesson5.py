"""Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().

"""

from homeworks import my_func as mf
import functools

my_test_list: list = list(el for el in mf.my_range(100, 1001) if not el & 1)
my_mega_numb = mf.my_reduce(lambda prev_el, el: prev_el * el, my_test_list)

# Проверка через reduce и range
test_list: list = list(el for el in range(100, 1001) if not el & 1)
mega_numb = functools.reduce(lambda prev_el, el: prev_el * el, test_list)

print(f"Каст. функция: {my_mega_numb}")
print(f"Встр. функция: {mega_numb}")

print(f"Разница: {my_mega_numb - mega_numb}")
