"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
from random import randint


limit = int(input('Введите желаемую длину массива: '))
array = [randint(1, 101) for _ in range(limit)]

first = {'idx': None, 'value': 100}
second = {'idx': None, 'value': 100}

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
