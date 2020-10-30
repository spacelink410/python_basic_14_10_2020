"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

"""

data: tuple = ()
hours_sum: int = 0
result: dict = {}

with open("files_input/in_task6.txt") as file:
    for line in file:
        hours_sum = 0
        data = line.partition(":")
        if data[0] != line:
            lesson = data[0].strip()
            hours_list = data[2].strip().split()
            for el in hours_list:
                hours_item = el.partition("(")
                if hours_item[0] != el:
                    hours_sum += int(hours_item[0])
            result.setdefault(lesson, hours_sum)

print(result)
