"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

"""

import random


def random_range_int(min_range=0, max_range=100, size_range=20):
    if max_range > min_range and size_range > 0:
        while size_range:
            yield str(random.randint(min_range, max_range))
            size_range -= 1


def my_reduce(func, iter_obj: list):
    while len(iter_obj) > 1:
        iter_obj.insert(0, func(iter_obj.pop(0), iter_obj.pop(0)))
    return iter_obj[0]


random_list = random_range_int(-2000, 2000)

with open("files_input/in_task5.txt", "w") as file:
    file.write(" ".join(random_list))

with open("files_input/in_task5.txt", "r") as file:
    line = file.readline()

digit_list = line.split()
try:
    out = my_reduce(lambda x, y: int(x) + int(y), digit_list)
    print(out)
except ValueError:
    print("Что-то пошло не так")
