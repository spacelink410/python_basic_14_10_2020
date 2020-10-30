"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""

# Универсальный способ исользовать гугл переводчик, предварительно установив его в окружение
# from googletrans import Translator
# trans = Translator()

data: list = []

# Будем переводить по словарю. Еще была идея слать json запроссы в translate.google.con
# и парсить от него json c переводом
tr_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("files_input/in_task4.txt") as file:
    for line in file:
        new_line = line.split(sep="—")
        first_word: str = new_line[0].strip()
        second_word: str = new_line[1].strip()
        if first_word in tr_dict:
            first_word = tr_dict[first_word]
        data.append(first_word + " — " + second_word + "\n")
        # ради интереса можно раскоментироать и проверить.
        # first = trans.translate(first, dest='ru', src='en').text

with open("files_output/out_task4.txt", "w") as file:
    file.writelines(data)
