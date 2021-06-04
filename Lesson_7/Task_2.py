"""
Отсортируйте по возрастанию методом слияния
    одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).

Выведите на экран исходный и отсортированный массивы.
"""
from random import uniform


def make_array():
    size = 20
    return [uniform(0, 50).__round__(2) for _ in range(size)]


def merge(left, right):
    result = []
    left_index, right_index = 0, 0
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
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(left, right)


if __name__ == '__main__':
    a = make_array()
    print(a)
    print(merge_sort(a))
