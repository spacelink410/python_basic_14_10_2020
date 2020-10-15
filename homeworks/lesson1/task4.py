"""

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.

"""

user_number: list = list(input("Введите целое положительное число: "))
buffer: int = 0
counter: int = 0

while counter < len(user_number):
    if int(user_number[counter]) > buffer:
        buffer = int(user_number[counter])
    counter += 1

print(f"Самая большая цифра: {buffer}")
