"""
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""
from random import randint


def make_array():
    print('Передайте параметры массива со случайными числами')
    min_point = int(input('Введите нижнюю границу диапозона: '))
    max_point = int(input('Введите верхнюю границу диапозона: '))
    limit = int(input('Введите желаемую длину массива: '))
    return [randint(min_point, max_point) for _ in range(limit)]


def get_even(array):
    for idx, value in enumerate(array):
        if not value & 1:
            result.append(idx)
    return result


if __name__ == '__main__':
    array = make_array()
    result = get_even(array)

    print(f'Индексы с четными значениями в массиве: {result}\n'
          f'Исходный список: {array}')
