"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.

"""


class Date:
    date_str: str = '21-13-2020'

    def __init__(self, date_str: str):
        self.date_str: str = date_str

    @classmethod
    def convert_date(cls, date_str: str = ''):
        """Преобразует строку в словарь с числовыми значениями даты в формете:
        {'day': 21, 'month': 12, 'year': 2020}

        :param date_str: для использования класса-метода со своим значением, а не из класса
        :return: словарь с данными о месяце.
        """

        # Ввел условие, чтобы посмотреть, как класс метод работает с аттрибутами класса
        if date_str == '':
            date_list: list = cls.date_str.split('-')
        else:
            date_list: list = date_str.split('-')

        try:
            date_data: dict = {'day': int(date_list[0]), 'month': int(date_list[1]), 'year': int(date_list[2])}
            return date_data
        except ValueError:
            print('Неверный формат даты')

    @staticmethod
    def validate_date(date_data: dict):
        if date_data['day'] < 1 or date_data['day'] > 31:
            print('День имеет неверное значение')
        elif date_data['month'] < 0 or date_data['month'] > 12:
            print('Месяц имеет неверное значение')
        else:
            return date_data


print(Date.convert_date('11-12-2020'))
print(Date.validate_date(Date.convert_date('11-13-2020')))
