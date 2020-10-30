"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.

"""

phrase: list = []
input_str: str = ''
i: int = 1

# сформируем данные для записи в файл
while True:
    input_str = input(f"Введите стоку {i}: ")
    if not len(input_str):
        break
    phrase.append(f"{i}: {input_str}\n")
    i += 1

# После этого сделаем запись в файл
try:
    with open(r"files_output/out_task1.txt", "w") as file:
        file.writelines(phrase)
except IOError:
    print("Ошибка чтения-записи файла")
