"""
1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков.

Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""
from collections import Counter
from random import randint
from timeit import timeit
import cProfile


def make_array(limit, min_point=0, max_point=100):
    """
    Вспомогательная функция для создания массива случайных чисел
    """
    return [randint(min_point, max_point) for _ in range(limit)]


def most_frequent_1(array: list):
    """
    Вариант c двумя циклами, без встроенных функций, для хранения результата используется словарь
    """
    num_count = {}
    result = {'num': 0, 'count': 0}
    for item in array:
        if item in num_count.keys():
            num_count[item] += 1
        else:
            num_count[item] = 1
    for num, count in num_count.items():
        if result['count'] < count:
            result['num'], result['count'] = num, count
    return result['num']


def most_frequent_2(array: list):
    """
    реализация через объект Counter встроенной библиотеки collections
    """
    return Counter(array).most_common(1)[0][0]


def most_frequent_3(array: list):
    """
    Улучшенный* вариант моей первой функции использует один цикл вместо двух
    для хранения результата использует переменную(не словарь) и также функцию count()
    """
    count = 0
    num = array[0]
    for i in array:
        current_count = array.count(i)
        if current_count > count:
            counter = current_count
            num = i
    return num


# алгоритм имеет линейную асимптотику, скорость исполнения возрастает синхронно увеличению объема данных
# в каждом шаге объем массива увеличивается в 10 раз, время выполнения увеличивается в 8-10 раз

# print(timeit('most_frequent_1(make_array(10))', number=1000, globals=globals()))       # 0.0086   10
# print(timeit('most_frequent_1(make_array(100))', number=1000, globals=globals()))      # 0.1203   100
# print(timeit('most_frequent_1(make_array(1000))', number=1000, globals=globals()))     # 0.7503   1000
# print(timeit('most_frequent_1(make_array(10_000))', number=1000, globals=globals()))   # 7.2500   10_000
# print(timeit('most_frequent_1(make_array(100_000))', number=1000, globals=globals()))  # 73.1201  100_000
# print(timeit('most_frequent_1(make_array(200_000))', number=1000, globals=globals()))  # 146.2416 200_000


# этот алгоритм тоже имеет линейную асипмтотику
# использование прекомпилированной библиотеки дает свои плоды в виде прироста 15 процентов производительности

# print(timeit('most_frequent_2(make_array(10))', number=1000, globals=globals()))       # 0.0100   10
# print(timeit('most_frequent_2(make_array(100))', number=1000, globals=globals()))      # 0.0702   100
# print(timeit('most_frequent_2(make_array(1000))', number=1000, globals=globals()))     # 0.6025   1000
# print(timeit('most_frequent_2(make_array(10_000))', number=1000, globals=globals()))   # 5.6916   10_000
# print(timeit('most_frequent_2(make_array(100_000))', number=1000, globals=globals()))  # 58.0524  100_000
# print(timeit('most_frequent_2(make_array(200_000))', number=1000, globals=globals()))  # 127.3754 200_000


# самый интересный опыт, алгоритм отказался выполняться при длине массива выше 1000 при том что я ждал более 10 минут
# производительность алгоритма резко падает после увеличения объема данных
# от 10 до 100 время увеличилось в 19 раз
# при увеличении длины массива со 100 до 1_000 производительность уменьшилась в 67 раз(!!!)


# print(timeit('most_frequent_3(make_array(10))', number=1000, globals=globals()))       # 0.0090   10
# print(timeit('most_frequent_3(make_array(100))', number=1000, globals=globals()))      # 0.1723   100
# print(timeit('most_frequent_3(make_array(1000))', number=1000, globals=globals()))     # 11.5925  1000
# print(timeit('most_frequent_3(make_array(10_000))', number=1000, globals=globals()))   # ERROR    10_000
# print(timeit('most_frequent_3(make_array(100_000))', number=1000, globals=globals()))  # ERROR    100_000
# print(timeit('most_frequent_3(make_array(200_000))', number=1000, globals=globals()))  # ERROR    200_000
