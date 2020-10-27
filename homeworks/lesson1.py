"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

"""

from sys import argv


def payroll_preparation(im_work_time, im_hour, im_prize=0.0):
    im_cost = im_work_time * im_hour + im_prize
    yield im_cost


try:
    script_name, first_name, last_name, work_time_hours, cost_hour, prize = argv
    cost = list(payroll_preparation(float(work_time_hours), float(cost_hour), float(prize)))
    print(f"{first_name} {last_name}, Заработная плата с учетом премии {prize} усл. ед. составляет {cost[0]} усл. ед.")
except TypeError:
    print("Ошибка типов передаваемых аргументов")
except ValueError:
    print("Переданы не все аргументы")
