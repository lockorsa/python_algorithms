"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
from random import randint


limit = int(input('Введите желаемую длину массива: '))
array = [randint(-100, 101) for _ in range(limit)]

result = {'index': None, 'value': -100}

for i, value in enumerate(array):
    if value < 0:
        if value > result['value']:
            result['index'], result['value'] = i, value

print(f"Максимальный отрицательный элемент находится под индексом {result['index']}, значение: {result['value']}\n"
      f"Исходный массив: {array}")
