'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def to_int(cls, date):
        str_list = date.split('-')
        int_list = [int(element) for element in str_list]
        return int_list


    @staticmethod
    def validate():
        int_list = Date.to_int(d.date)
        for element in int_list:
            if len(str(element)) == 4:
                print(f'Число {element} - год')
            elif len(str(element)) == 2:
                print(f'Число {element} - день')
            elif len(str(element)) == 1:
                print(f'Число {element} - месяц')

d = Date('29-7-2021')

print(Date.validate())