"""
4. Определить, какое число в массиве встречается чаще всего.
"""
from random import randint


limit = int(input('Введите желаемую длину массива: '))
array = [randint(1, 101) for _ in range(limit)]
num_count = {}

for el in array:
    if el in num_count.keys():
        num_count[el] += 1
    else:
        num_count[el] = 1

result = {'digit': 0, 'count': 0}

for num, count in num_count.items():
    if result['count'] < count:
        result['digit'], result['count'] = num, count

print(f'Чаще всего в массиве встречается цифра {result["digit"]}, {result["count"]} раз/а\n'
      f'Исходный массив: {array}')
