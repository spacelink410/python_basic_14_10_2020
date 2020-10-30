"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

"""

# знаю про with. захотелось попробовать просто open
file = open("files_input/in_task3.txt")
data = file.readlines()
file.close()

employees_money_sum: float = 0

print("Оклад менее 20 тыс. имеют сотрудники:")

line_count: int = 1
valid_employees_cont: int = 0

for el in data:
    employee_data_list = el.split()

    try:
        if float(employee_data_list[1]) < 20000:
            print(employee_data_list[0])

        employees_money_sum += float(employee_data_list[1])
        valid_employees_cont += 1

    except IndexError:
        print(f"Ошибка данных в строке {line_count}")

    except ValueError:
        print(f"Ошибка данных в строке {line_count}")

    line_count += 1

print(f"\nСредний доход сотрудников: {employees_money_sum / valid_employees_cont}")
