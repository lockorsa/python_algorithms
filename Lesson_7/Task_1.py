"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).

Выведите на экран исходный и отсортированный массивы.

Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
    Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
from random import randint


def make_array():
    size = 20
    return [randint(-100, 100) for _ in range(size)]


def bubble_sort(arr):
    res = arr.copy()

    for i in range(len(arr)):
        break_flag = True

        for j in range(len(arr) - i - 1):
            if res[j] < res[j + 1]:
                res[j], res[j+1] = res[j+1], res[j]
                break_flag = False
        if break_flag:
            break
    return res


if __name__ == '__main__':
    a = make_array()
    print(a)
    print(bubble_sort(a))
