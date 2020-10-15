"""

Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

"""

first_day_distance: float = float(input("Введите количество км за первый день: "))
total_result: float = float(input("Сколько км необходимо пробежать: "))
middle_result: float = first_day_distance
days: int = 1

while middle_result <= total_result:
    middle_result += middle_result * 0.1
    days += 1

print(f"\nНа {days}-й день спортсмен достигнет результата — не менее {total_result} км. ")
