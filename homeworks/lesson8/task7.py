"""Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.

"""


class CPlex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        operator = "+"
        operator = "-" if self.img < 0 else operator
        return str(self.real) + operator + str(abs(self.img)) + 'j'

    def __add__(self, other):
        self.sum_real = self.real + other.real
        self.sum_img = self.img + other.img
        operator = "+"
        operator = "-" if self.sum_img < 0 else operator
        return str(self.sum_real) + operator + str(abs(self.sum_img)) + 'j'

    def __mul__(self, other):
        self.mul_real = self.real * other.real - self.img * other.img
        self.mul_img = self.img * other.real + self.real * other.img
        operator = "+"
        operator = "-" if self.mul_img < 0 else operator
        return str(self.mul_real) + operator + str(abs(self.mul_img)) + 'j'


c1 = CPlex(-45, 98)
c2 = CPlex(4.5, 0.34)
print(f"\nЧисло 1: {c1}")
print(f"Число 2: {c2}")

total = c1 + c2
print(f"\nРезультат сложения: {total}")
total2 = complex(c1.__str__()) + complex(c2.__str__())
print(f"Результат сложения проверочный: {total2}")

total = c1 * c2
print(f"\nРезультат умножения: {total}")
total2 = complex(c1.__str__()) * complex(c2.__str__())
print(f"Результат умножения проверочный: {total2}")
