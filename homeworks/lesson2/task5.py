"""

Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

"""
default_list: list = [6, 5, 5, 4, 3]
# default_list: list = []

while True:
    user_sym: str = input("Введите число для вставки или 'n' чтобы выйти: ")

    if user_sym == 'n':
        break

    user_digit: int = int(user_sym)

    if user_digit <= 0:
        print(f"Число {user_digit} не является натуральным")
    elif len(default_list) == 0:
        default_list.append(user_digit)
    elif user_digit == 1:
        default_list.append(user_digit)
    elif user_digit > default_list[0]:
        default_list.insert(0, user_digit)
    else:
        for el in default_list:
            if user_digit > el:
                default_list.insert(default_list.index(el), user_digit)
                break
            elif user_digit == el:
                # берем совпадаюший элемент и прибавляем количество таких же, если есть
                new_index: int = default_list.index(user_digit) + default_list.count(user_digit)
                default_list.insert(new_index, user_digit)
                break
            elif user_digit < el:
                if default_list.index(el) == len(default_list) - 1:
                    default_list.append(user_digit)
                    break
                else:
                    continue

    print(default_list)
