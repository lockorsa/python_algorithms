"""
Отсортируйте по возрастанию методом слияния
    одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).

Выведите на экран исходный и отсортированный массивы.
"""
from random import randint


def make_array():
    size = 20
    return [randint(1, 50) for _ in range(size)]


def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:
        return array

    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)


if __name__ == '__main__':
    a = make_array()
    print(a)
    print(merge_sort(a))
