"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.

"""

import json

company_data_list: list = []
company_dict: dict = {}
average_dict: dict = {}
json_list: list = []
profit_sum: float = 0
file_name_counter: int = 1
count: int = 0

with open("files_input/in_task7.txt") as file:
    for line in file:
        company_data_list.append(line.strip().split())

for el in company_data_list:
    profit = int(el[2]) - int(el[3])

    # В ситуации, если наименование фирм совпадает, переименуем их, чтобы не потерять
    # Воспользуемся формой собственности.
    # Если они будут полностью идентичны то возьмем последнее значение.
    if el[0] in company_dict:
        el[0] = el[0] + f"_" + el[1]
        file_name_counter += 1

    company_dict.setdefault(el[0], profit)
    if profit > 0:
        profit_sum += profit
        count += 1

average_dict.setdefault("average_profit", profit_sum/count)

json_list.append(company_dict)
json_list.append(average_dict)

with open("files_output/out_task7.txt", "w") as write_f:
    json.dump(json_list, write_f)
