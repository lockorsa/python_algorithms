"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
from random import randint


def make_array():
    print('Передайте параметры массива со случайными числами')
    min_point = int(input('Введите нижнюю границу диапозона: '))
    max_point = int(input('Введите верхнюю границу диапозона: '))
    limit = int(input('Введите желаемую длину массива: '))
    return [randint(min_point, max_point) for _ in range(limit)]


def max_negative(array):
    result = {'idx': None, 'value': float('inf')}
    for idx, value in enumerate(array):
        if value < 0:
            if value > result['value']:
                result['idx'] = idx
                result['value'] = value
    if not result['idx'] is None:
        return result
    else:
        raise Exception('Вы передали массив без отрицательных элементов')


if __name__ == '__main__':
    array = make_array()
    result = max_negative(array)
    print(f'Индекс макисмального отрицательного элемента - {result["idx"]}, значение - {result["value"]}')
