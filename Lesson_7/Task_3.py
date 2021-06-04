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
    arr_copy = arr.copy()
    middle = len(arr) // 2 + 1
    tmp = 0
    for _ in range(middle):
        lowest = arr_copy[0]
        for i in arr_copy:
            if i < lowest:
                lowest = i
        arr_copy.remove(lowest)
        tmp += 1
        if tmp >= middle:
            return lowest


if __name__ == '__main__':
    a = make_array()
    print(a, sorted(a), sep='\n')
    print(find_median(a))
