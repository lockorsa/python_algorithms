"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint


limit = int(input('Введите желаемую длину массива: '))
array = [randint(1, 101) for _ in range(limit)]

maximum = {'index': None, 'value': 0}
minimum = {'index': None, 'value': 101}

# находим пару индекс/значение для максимального и минимального числа
for i, value in enumerate(array):
    if value > maximum['value']:
        maximum['index'], maximum['value'] = i, value
    elif value < minimum['value']:
        minimum['index'], minimum['value'] = i, value

result = 0
for i in range(minimum['index'] + 1, maximum['index']):
    result += array[i]

print(f'Исходный массив: {array}\n'
      f'Индекс/значение минимального элемента - ({minimum["index"]}, {minimum["value"]}), '
      f'максимального - ({maximum["index"]}, {maximum["value"]})\n'
      f'Сумма элементов между ними - {result}')
