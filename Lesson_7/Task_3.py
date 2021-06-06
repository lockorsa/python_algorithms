"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
    в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
(сортировка слиянием также недопустима).
"""
from random import randint


def make_array():
    size = 21
    return [randint(1, 50) for _ in range(size)]


def find_median(arr):
    array = arr.copy()
    middle = len(arr) // 2 + 1
    for _ in range(middle):
        lowest = array[0]
        for i in array:
            if i < lowest:
                lowest = i
        array.remove(lowest)
    return lowest


if __name__ == '__main__':
    a = make_array()
    print(a, sorted(a), find_median(a), sep='\n')
