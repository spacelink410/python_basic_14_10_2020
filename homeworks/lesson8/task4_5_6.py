"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.


Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Storage:
    def __init__(self, name: str):
        self.name = name
        self.__container = {}
        self.__counter: dict = {}

    def add_office_eq_to_storage(self, *args):
        """Метод добавления экземпляров классов в коллекцию с ведением подсчета
        количества объектов в отдельном словаре
        Классы добавляются в структуру:
        {'Printer': [<__main__.Printer object at 0x10e7622e8>, <__main__.Printer object at 0x10e762320>],
         'Scanner': [<__main__.Scanner object at 0x10e7623c8>],
         'Xerox': [<__main__.Xerox object at 0x10e7624a8>]}
        Счетчик срхраняет данные в словарь:
        {'Printer': 4, 'Scanner': 4, 'Xerox': 3}

        :param args: объекты классов
        :return: None
        """

        for el in args:
            if self.__counter.get(el.__class__.__name__):
                self.__container[el.__class__.__name__].append(el)
                self.__counter[el.__class__.__name__] = self.__counter.get(el.__class__.__name__) + 1
            else:
                self.__container.setdefault(el.__class__.__name__, [el])
                self.__counter.setdefault(el.__class__.__name__, 1)

    def __getitem__(self, item, eq_obj):
        """Метод полученя объекта из коллекции. Переопределяет стандартный метод,
        изымает элемент из коллекци и возвращает изъятый объект экземпляр класса.
        При этом уменьшает значение счетчика объектов

        :param item:
        :param eq_obj:
        :return:
        """

        try:
            eq_list: list = self.__container[item]
            for idx in range(len(eq_list)):
                if eq_obj is eq_list[idx]:
                    eq = eq_list.pop(idx)
                    self.__container[item] = eq_list
                    self.__counter[eq_obj.__class__.__name__] = self.__counter.get(eq_obj.__class__.__name__) - 1
                    return eq
            else:
                return None
        except IndexError:
            print('Такого устройства нет!')
        except KeyError:
            print(f'Устройств {item} нет!')

    def move_eq_to(self, dep_to, eq_obj):
        """Метод перемещает искомый объект из одной коллекции, экземпляры, вызвавщего метод в другую
        коллекцию, указанную в качестве параметра

        :param dep_to: коллекция, куда необходимо переместить объект
        :param eq_obj: объект, которые необходимо переместить
        :return: None
        """

        eq_obj = self.__getitem__(eq_obj.__class__.__name__, eq_obj)
        if eq_obj:
            dep_to.add_office_eq_to_storage(eq_obj)
        else:
            print('Нет устройства для перемещения')

    @property
    def storage_info(self):
        """Метод получения информации о том сколько и каких объектов хранится в коллекции

        :return: список, хранящий в первом элементе словарь со счетчиками, а во втором словарь
        с объектами, хранящимися в коллекции:
        [{'Printer': 1}, {'Printer': [<__main__.Printer object at 0x10e7622e8>]}]
        """

        return [self.__counter, self.__container]


class OfficeEq:
    def __init__(self,
                 name: str,
                 inventory: int):
        self.name = name
        self.inventory = inventory


class Printer(OfficeEq):
    def __init__(self,
                 name,
                 inventory,
                 print_type: str):
        super().__init__(name, inventory)
        self.print_type = print_type


class Scanner(OfficeEq):
    def __init__(self,
                 name,
                 inventory,
                 scanning_speed: str):
        super().__init__(name, inventory)
        self.scanning_speed = scanning_speed


class Xerox(OfficeEq):
    def __init__(self,
                 name,
                 inventory,
                 form_factor: str):
        super().__init__(name, inventory)
        self.form_factor = form_factor


# Создадим склад и it-отдел
storage = Storage('Склад')
it_dep = Storage('IT - отдел')

# Срздадим принтеры, сканеры, ксероксы. Кстати, ксерокс - это фирма, а не устройство))
p = Printer('ML1200', 123218376, 'Laser')
p1 = Printer('ML1200', 123218377, 'Laser')
p2 = Printer('ML1200', 123218378, 'Laser')
p3 = Printer('ML1200', 123218379, 'Laser')

s = Scanner('SC23', 234543534, '12 стр/мин')
s1 = Scanner('SC23', 234543535, '12 стр/мин')
s2 = Scanner('SC23', 234543536, '12 стр/мин')
s3 = Scanner('SC23', 234543537, '12 стр/мин')

x = Xerox('XC23', 3485723023, 'desk')
x1 = Xerox('XC29', 3485723024, 'MFU')
x2 = Xerox('XC301', 3485723025, 'floor')
x3 = Xerox('XC301', 3485723026, 'floor')

# добавим на склад все созданные устройства
storage.add_office_eq_to_storage(p, p1, p2, p3, s, s1, s2, s3, x, x1, x2)

# Просмотрим количество и список объектов на складе
print("\nПервоначальное состояние склада \n", storage.storage_info)

# Переместим некоторые устройства в it-отдел
storage.move_eq_to(it_dep, x2)
storage.move_eq_to(it_dep, s2)
storage.move_eq_to(it_dep, p2)

# Посмотрим, что устройства нужных типов переместились со склада в it-отдел
print("\nСостояние склада после перемещения 3-х предметов \n", storage.storage_info)
print(f"\nСостояние it-отдела после перемещения 3-х предметов \n{it_dep.storage_info}\n")

# Попробуем снова переместить ксерокс x2 в it-отдел и получим сообщение, что его нет на складе
storage.move_eq_to(it_dep, x2)

# Посмотрим, что количество устройств на скалде и it-отделе не имзенилось
print("\nСостояние склада после ошибки перемещения ксерокса \n", storage.storage_info)
print(f"\nСостояние it-отдела после ошибки перемещения ксерокса\n{it_dep.storage_info}")

# Вернем ксерокс на скалд из it-отдела
it_dep.move_eq_to(storage, x2)

# Посмотрим, как количество устройств на скалде и it-отделе имзенилось
print("\nСостояние склада после перемещения ксерокса \n", storage.storage_info)
print(f"\nСостояние it-отдела после перемещения ксерокса\n{it_dep.storage_info}")
