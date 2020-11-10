""" Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.

"""


class MyError(Exception):
    def __init__(self, text):
        self.text = text


try:
    a, b = input("Введите делимое и делитель чере пробел: ").split()
    a, b = float(a), float(b)
    if b == 0:
        raise MyError("Деление на ноль!")
except ValueError:
    print("Введеныые значения имеют нечисловой формат")
except MyError as err:
    print(err)
else:
    result = a / b
    print(result)
