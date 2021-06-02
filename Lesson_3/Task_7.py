"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
from random import randint


def make_array():
    print('Передайте параметры массива со случайными числами')
    min_point = int(input('Введите нижнюю границу диапозона: '))
    max_point = int(input('Введите верхнюю границу диапозона: '))
    limit = int(input('Введите желаемую длину массива: '))
    return [randint(min_point, max_point) for _ in range(limit)]


def get_two_min(array):
    first = {'idx': None, 'value': float('inf')}
    second = {'idx': None, 'value': float('inf')}
    for idx, value in enumerate(array):
        if value < first['value']:
            first['idx'] = idx
            first['value'] = value
    for idx, value in enumerate(array):
        if not idx == first['idx']:
            if value < second['value']:
                second['idx'] = idx
                second['value'] = value
    return first['value'], second['value']


if __name__ == '__main__':
    array = make_array()
    result = get_two_min(array)

    print(f'Исходный массив: {array}\n'
          f'Самый маленький элемент в массиве - {result[0]}\n'
          f'Второй минимальный элемент {result[1]}')
