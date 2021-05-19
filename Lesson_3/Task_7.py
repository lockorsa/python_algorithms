"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
from random import randint


def make_array(min_point, max_point, limit):
    return [randint(min_point, max_point + 1) for _ in range(limit)]


print('Передайте параметры массива со случайными числами')
min_point = int(input('Введите нижнюю границу диапозона: '))
max_point = int(input('Введите верхнюю границу диапозона: '))
limit = int(input('Введите желаемую длину массива: '))
array = make_array(min_point, max_point, limit)

first = {'idx': None, 'value': max_point}
second = {'idx': None, 'value': max_point}

for idx, value in enumerate(array):
    if value < first['value']:
        first['idx'] = idx
        first['value'] = value

for idx, value in enumerate(array):
    if not idx == first['idx']:
        if value < second['value']:
            second['idx'] = idx
            second['value'] = value

print(f'Исходный массив: {array}\n'
      f'Самый маленький элемент в массиве - {first["value"]}, индекс - {first["idx"]}\n'
      f'Второй минимальный элемент {second["value"]}, индекс - {second["idx"]}')
