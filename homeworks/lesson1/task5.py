"""

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

"""

company_income: float = float(input("Введите значение выручки: "))
company_costs: float = float(input("Введите значение издержек: "))

if company_costs < company_income:
    print("\nФирма работает с прибылью")
    company_profit: float = company_income - company_costs
    company_profit_rel: float = company_profit / company_income * 100
    print(f"Рентабельнсть фирмы {company_profit_rel:4.2f}%")
    company_staff: int = int(input("\nВведите чсло сотрудников фирмы: "))
    company_staff_profit: float = company_profit / company_staff
    print(f"Прибыль в пересчете на 1 сотрудника: {company_staff_profit:4.2f}")
else:
    print("\nФирма работает в убыток")
