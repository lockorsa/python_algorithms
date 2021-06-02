"""
4. Определить, какое число в массиве встречается чаще всего.
"""
from random import randint


def make_array():
    print('Передайте параметры массива со случайными числами')
    min_point = int(input('Введите нижнюю границу диапозона: '))
    max_point = int(input('Введите верхнюю границу диапозона: '))
    limit = int(input('Введите желаемую длину массива: '))
    return [randint(min_point, max_point) for _ in range(limit)]


def most_common(array):
    num_counter = {}
    result = {'num': 0, 'count': 0}
    for el in array:
        if el in num_counter.keys():
            num_counter[el] += 1
        else:
            num_counter[el] = 1
    for num, count in num_counter.items():
        if result['count'] < count:
            result['num'] = num
            result['count'] = count
    return result


if __name__ == '__main__':
    array = make_array()
    result = most_common(array)
    print(f'Чаще всего в массиве встречается цифра {result["num"]}, {result["count"]} раз/а\n'
          f'Исходный массив: {array}')
