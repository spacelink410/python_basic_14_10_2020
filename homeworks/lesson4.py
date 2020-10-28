"""Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]

"""

from homeworks import my_func as mf

# сгенерируем рандомный список. документацию см. в модуле my_func.py
default_list: list = list(mf.random_range_int(1, 10, 10))
result_list: list = []
result_list = list(el for el in default_list if default_list.count(el) == 1)

print(default_list)
print(result_list)
