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
maximum = {'idx': None, 'value': min_point}
minimum = {'idx': None, 'value': max_point}
result = 0

# находим пару индекс/значение для максимального и минимального числа
for idx, value in enumerate(array):
    if value > maximum['value']:
        maximum['idx'], maximum['value'] = idx, value
    elif value < minimum['value']:
        minimum['idx'], minimum['value'] = idx, value

for i in range(minimum['idx'] + 1, maximum['idx']):
    result += array[i]

print(f'Исходный массив: {array}\n'
      f'Индекс/значение минимального элемента - ({minimum["idx"]}, {minimum["value"]}), '
      f'максимального - ({maximum["idx"]}, {maximum["value"]})\n'
      f'Сумма элементов между ними - {result}')
