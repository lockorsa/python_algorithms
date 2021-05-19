"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint


def make_array(min_point, max_point):
    limit = int(input('Введите желаемую длину массива: '))
    return [randint(min_point, max_point + 1) for _ in range(limit)]


print('Передайте параметры массива со случайными числами')
min_point = int(input('Введите нижнюю границу диапозона: '))
max_point = int(input('Введите верхнюю границу диапозона: '))

array = make_array(min_point, max_point)
maximum = {'index': None, 'value': min_point}
minimum = {'index': None, 'value': max_point}

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
