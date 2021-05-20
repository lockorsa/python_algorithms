"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint


def make_array(min_point, max_point):
    limit = int(input('Введите желаемую длину массива: '))
    return [randint(min_point, max_point) for _ in range(limit)]


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

if minimum['idx'] < maximum['idx']:
    for i in range(minimum['idx'] + 1, maximum['idx']):
        result += array[i]
else:
    for i in range(maximum['idx'] + 1, minimum['idx']):
        result += array[i]

print(f'Исходный массив: {array}\n'
      f'Минимальный элемент - {minimum["value"]}, индекс - {minimum["idx"]}\n'
      f'Максимальный элемент - {maximum["value"]}, индекс - {maximum["idx"]}\n'
      f'Сумма элементов между ними - {result}')
