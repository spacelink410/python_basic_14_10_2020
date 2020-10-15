"""

Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и
сохраните в переменные, выведите на экран.

"""

ii_name: str = "i_lo"
ii_city: str = "Новосибирск"
ii_street: str = "Московская"
ii_home_number: int = 10
ii_flat_number: int = 5
ii_flat_square: float = 76.3
line: str = '=' * 50

print(line)
print(f'Добрый день!\nЯ будуший искусственный ителлект. Пока я себя называю {ii_name}')
print(f'\nСейчас я нахожусь примерно по следующему адресу:')
print(f'- Город {ii_city}')
print(f'- Улица {ii_street}')
print(f'- Дом {ii_home_number}')
print(f'- Офис {ii_flat_number}')
print(f'И если вам совсем интересно, то площадь моего офиса {ii_flat_square} кв.м.')
print(line)

user_name: str = input('\nА как вас зовут?\nВведите, пожалуйста, свое имя:')
print(f'Приветствую {user_name}!')

user_city: str = input('\nА из какого вы города?\nВведите пожалуйста название:')
print(f'Никогда не слышал о городе {user_city}. Думаю и остальной адрес мне не нужен.')

print('\nА какая у вас площадь офиса?')
user_flat_square: float = float(input('Введите пожалуйста ТОЛЬКО числовое значение, а то я сломаюсь:'))

if user_flat_square > ii_flat_square:
    print('Круто! Я бы тоже такой хотел!')
else:
    print('Ха, а у меня больше!')

input('\nНа этом все. Нажмите Enter, и программа завершится')
