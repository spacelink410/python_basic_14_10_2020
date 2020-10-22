"""

Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

"""


def my_div(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "ZeroDivisionError"
    except TypeError:
        return "TypeError"


while True:
    try:
        user_num = float(input("\nВведите числитель: "))
        user_den = float(input("Введите знаменатель: "))
        if my_div(user_num, user_den) == "ZeroDivisionError":
            print("Деление на ноль!")
        elif my_div(user_num, user_den) == "TypeError":
            print("Неподдерживаемые операнды для операции /")
        else:
            print(f"\n{user_num} / {user_den} = {my_div(user_num, user_den)}")
    except ValueError:
        print("Введенное значение не является числом!")

    if input("\nЗавершить? Введите 'n' для завершения") == 'n':
        break
