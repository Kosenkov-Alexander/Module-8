'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''

'''
5. Продолжить работу над первым заданием. 
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
'''

'''
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
'''

class IntError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    items = {}

    def give_to_department(self, name_department, name_office_equip):
        amount_to_give = 1
        name_department.dep_office_equip[name_office_equip] = {'model':self.items[name_office_equip]['model'],
                                               'price': self.items[name_office_equip]['price'],
                                               'is_color': self.items[name_office_equip]['is_color'],
                                               'amount': amount_to_give
                                               }
        self.items[name_office_equip]['amount'] -= amount_to_give
        print(f'Предмет {name_office_equip} был передан в {name_department}')
        print(f'Таких предметов как {name_office_equip} на складе осталось {self.items[name_office_equip]["amount"]}\n')


class OfficeEquipment:
    def __init__(self, model, price, is_color, amount):
        self.model = model
        self.price = price
        self.is_color = is_color
        self.amount = amount


class Printer(OfficeEquipment):
    def __init__(self, model, price, is_color, amount):
        super().__init__(model, price, is_color, amount)

    def __str__(self):
        return 'Принтер'

    def give_to_warehouse(self):
        while True:
            try:
                amount_to_give = input(f'Сколько предметов передать на склад, в данный момент в наличии {self.amount}: ')
                if amount_to_give.isdigit():
                    amount_to_give = int(amount_to_give)
                    break
                else:
                    raise IntError('Вы ввели не число, а букву. Необходимо ввести число')
            except IntError as ie:
                print(ie)

        warehouse.items[self.__class__.__name__] = {'model': self.model,
                                                    'price': self.price,
                                                    'is_color': self.is_color,
                                                    'amount': amount_to_give}
        self.amount -= amount_to_give
        print(f'Принтер(ы) в количестве: {amount_to_give} штук переданы на склад. Остаток: {self.amount}\n')


class Scanner(OfficeEquipment):
    def __init__(self, model, price, is_color, amount):
        super().__init__(model, price, is_color, amount)

    def __str__(self):
        return 'Сканнер'

    def give_to_warehouse(self):
        while True:
            try:
                amount_to_give = input(
                    f'Сколько предметов передать на склад, в данный момент в наличии {self.amount}: ')
                if amount_to_give.isdigit():
                    amount_to_give = int(amount_to_give)
                    break
                else:
                    raise IntError('Вы ввели не число, а букву. Необходимо ввести число')
            except IntError as ie:
                print(ie)
        warehouse.items[self.__class__.__name__] = {'model': self.model,
                                                    'price': self.price,
                                                    'is_color': self.is_color,
                                                    'amount': amount_to_give}
        self.amount -= amount_to_give
        print(f'Сканнер(ы) в количестве: {amount_to_give} штук переданы на склад. Остаток: {self.amount}\n')


class Xerox(OfficeEquipment):
    def __init__(self, model, price, is_color, amount):
        super().__init__(model, price, is_color, amount)

    def __str__(self):
        return 'Ксерокс'

    def give_to_warehouse(self):
        while True:
            try:
                amount_to_give = input(
                    f'Сколько предметов передать на склад, в данный момент в наличии {self.amount}: ')
                if amount_to_give.isdigit():
                    amount_to_give = int(amount_to_give)
                    break
                else:
                    raise IntError('Вы ввели не число, а букву. Необходимо ввести число')
            except IntError as ie:
                print(ie)
        warehouse.items[self.__class__.__name__] = {'model': self.model,
                                                    'price': self.price,
                                                    'is_color': self.is_color,
                                                    'amount': amount_to_give}
        self.amount -= amount_to_give
        print(f'Ксерокс(ы) в количестве: {amount_to_give} штук переданы на склад. Остаток: {self.amount}\n')


class Department:
    def __init__(self, dep_office_equip):
        self.dep_office_equip = dep_office_equip


class Finance(Department):
    def __init__(self, dep_office_equip):
        super().__init__(dep_office_equip)

    def __str__(self):
        return 'Финансовый департамент'


class It(Department):
    def __init__(self, dep_office_equip):
        super().__init__(dep_office_equip)

    def __str__(self):
        return 'Департамент информационных технологий'


printer = Printer('Hp', 15000, True, 3)
scanner = Scanner('Canon', 23000, True, 4)
xerox = Xerox('Hp', 7000, False, 5)

warehouse = Warehouse()
finance = Finance({})
it = It({})


printer.give_to_warehouse()
# scanner.give_to_warehouse()

warehouse.give_to_department(name_department=finance, name_office_equip='Printer')
# warehouse.give_to_department(name_department=it, name_office_equip='Scanner')
