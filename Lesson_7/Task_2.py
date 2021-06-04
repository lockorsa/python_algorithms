"""
Отсортируйте по возрастанию методом слияния
    одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).

Выведите на экран исходный и отсортированный массивы.
"""
from random import randint


def make_array():
    size = 20
    return [randint(1, 50) for _ in range(size)]


def merge_sort(arr):
    middle = len(arr) // 2  # + 1 if len(arr) % 2 == 1 else len(arr) // 2
    left, right = arr[:middle], arr[:middle]

    return middle


if __name__ == '__main__':
    a = make_array()
    print(a)
    print(a[:10], a[10:])
    print(merge_sort(a))
