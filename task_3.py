'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
'''

my_list = []
class IntError(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
        user_number = input('Введите число: ')
        if user_number == 'stop':
            print(my_list)
            break
        if user_number.isdigit():
            my_list.append(int(user_number))
        else:
            raise IntError('Вы ввели не число!')
    except IntError as ie:
        print(ie)
