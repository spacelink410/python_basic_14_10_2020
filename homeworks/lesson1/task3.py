"""

Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

"""

user_number: str = input("введите целое число: ")

term2: str = user_number * 2
term3: str = user_number * 3
total: int = int(user_number) + int(term2) + int(term3)

print(f"Итого сумма {user_number} + {term2} + {term3} = {total}")
