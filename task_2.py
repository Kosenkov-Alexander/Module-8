'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

number = 100

try:
    div_number = int(input('Введите число: '))
    if div_number == 0:
        raise OwnError('Пользователь пытается поделить на 0')
    result = number / div_number
except ValueError:
    print('Пользователь пытается поделить на строку')
except OwnError as oe:
    print(oe)
else:
    print(result)



