"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

"""

words_count: int = 0

with open("files_input/in_task2.txt", "r") as file:
    files_data: list = file.readlines()

print(f"Количество строк: {len(files_data)}")

# не будем цепляться к понятию слова и примем, что одиночные знаки и символы являются словами
# иначе в будущем будем чистить строки
i: int = 1
for el in files_data:
    words_count = len(el.split())
    print(f"Количество слов в строке {i} - {words_count}")
    i += 1
