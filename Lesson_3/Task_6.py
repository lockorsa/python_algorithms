"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint


def make_array():
    print('Передайте параметры массива со случайными числами')
    min_point = int(input('Введите нижнюю границу диапозона: '))
    max_point = int(input('Введите верхнюю границу диапозона: '))
    limit = int(input('Введите желаемую длину массива: '))
    return [randint(min_point, max_point) for _ in range(limit)]


def sum_between(array):
    result = 0
    maximum = {'idx': None, 'value': float('-inf')}
    minimum = {'idx': None, 'value': float('inf')}

    for idx, value in enumerate(array):
        if value > maximum['value']:
            maximum['idx'], maximum['value'] = idx, value
        elif value < minimum['value']:
            minimum['idx'], minimum['value'] = idx, value

    if minimum['idx'] > maximum['idx']:
        minimum['idx'], maximum['idx'] = maximum['idx'], minimum['idx']

    for i in range(minimum['idx'] + 1, maximum['idx']):
        result += array[i]

    return result


if __name__ == '__main__':
    array = make_array()
    result = sum_between(array)

    print(f'Исходный массив: {array}\n'
          f'Сумма элементов между минимальным и максимальным элементами - {result}')
