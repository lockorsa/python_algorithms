"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
from random import randint


def make_array(min_point, max_point):
    limit = int(input('Введите желаемую длину массива: '))
    return [randint(min_point, max_point + 1) for _ in range(limit)]


print('Передайте параметры массива со случайными числами')
min_point = int(input('Введите нижнюю границу диапозона: '))
max_point = int(input('Введите верхнюю границу диапозона: '))

array = make_array(min_point, max_point)
result = {'idx': None, 'value': max_point}

for idx, value in enumerate(array):
    if value < 0:
        if value > result['value']:
            result['idx'] = idx
            result['value'] = value

print(f"Максимальный отрицательный элемент находится под индексом {result['index']}, значение: {result['value']}\n"
      f"Исходный массив: {array}")
