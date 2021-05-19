"""
4. Определить, какое число в массиве встречается чаще всего.
"""
from random import randint


def make_array(min_point, max_point, limit):
    return [randint(min_point, max_point + 1) for _ in range(limit)]


print('Передайте параметры массива со случайными числами')
min_point = int(input('Введите нижнюю границу диапозона: '))
max_point = int(input('Введите верхнюю границу диапозона: '))
limit = int(input('Введите желаемую длину массива: '))
array = make_array(min_point, max_point, limit)

num_count = {}

for el in array:
    if el in num_count.keys():
        num_count[el] += 1
    else:
        num_count[el] = 1

result = {'num': 0, 'count': 0}

for num, count in num_count.items():
    if result['count'] < count:
        result['num'],  = num
        result['count'] = count

print(f'Чаще всего в массиве встречается цифра {result["num"]}, {result["count"]} раз/а\n'
      f'Исходный массив: {array}')
