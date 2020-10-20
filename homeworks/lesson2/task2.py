"""

Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

"""

# список по дефолту, чтобы не набивать данными
user_list: list = [1, "text", True, (0, 1), 2.24, {0, 1}, [1, 2], 10, 11]

"""

список из строк разбитых черех пробел
user_list_2: list = input("Введите данные через пробел").split()
print(user_list_2)

"""

# было интересно для себя сделать полу умную заполнялку списка разными типами
# данный блок при желании переопределяет дефолтный список
if input("Хотите создать свой список? 'y' or 'n'") == "y":
    user_list.clear()
    while True:
        user_list_data = input("Введите тип данных int, float, string, list, tuple: ")
        if user_list_data == "int":
            user_list.append(int(input("Введите значение для добаления в список: ")))
        elif user_list_data == "float":
            user_list.append(float(input("Введите значение для добаления в список: ")))
        elif user_list_data == "list":
            user_list.append(list(input("Введите значение для добаления в список: ")))
        elif user_list_data == "tuple":
            user_list.append(tuple(input("Введите значение для добаления в список: ")))
        else:
            user_list.append(str(input("Введите значение для добаления в список: ")))

        if input("Введите 'y' если хотите завершить наполнение данных: ") == "y":
            break

count: int = len(user_list)
if count > 1:
    if count % 2 != 0:
        count -= 2
    else:
        count -= 1
    while count >= 1:
        user_list[count], user_list[count-1] = user_list[count-1], user_list[count]
        count -= 2
else:
    print("Ничего не меняем")

print(user_list)

