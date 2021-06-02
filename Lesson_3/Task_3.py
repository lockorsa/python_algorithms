"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
from random import randint


def make_array():
    print('Передайте параметры массива со случайными числами')
    min_point = int(input('Введите нижнюю границу диапозона: '))
    max_point = int(input('Введите верхнюю границу диапозона: '))
    limit = int(input('Введите желаемую длину массива: '))
    return [randint(min_point, max_point) for _ in range(limit)]


def switch_min_max(array):
    result = array.copy()
    maximum = {'idx': None, 'value': float('-inf')}
    minimum = {'idx': None, 'value': float('inf')}
    for idx, value in enumerate(array):
        if value > maximum['value']:
            maximum['idx'] = idx
            maximum['value'] = value
        elif value < minimum['value']:
            minimum['idx'] = idx
            minimum['value'] = value
    result[minimum['idx']] = maximum['value']
    result[maximum['idx']] = minimum['value']
    return result


if __name__ == '__main__':
    array = make_array()
    result = switch_min_max(array)
    print(f'Исходный массив: {array}\n'
          f'Преобразованный массив: {result}')
