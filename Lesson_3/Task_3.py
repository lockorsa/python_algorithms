"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
from random import randint


limit = int(input('Введите желаемую длину массива: '))
array = [randint(1, 101) for _ in range(limit)]

# max_value[0] - индекс, max_value[1] - значение
max_value, min_value = [0, 0], [0, 100]

# находим пару индекс/значение для максимального и минимального числа
for i, value in enumerate(array):
    if value > max_value[1]:
        max_value = [i, value]
    elif value < min_value[1]:
        min_value = [i, value]

print(f'Исходный массив: {array}\n'
      f'Индекс наименьшего элемента: {min_value[0]}, значение: {min_value[1]}\n'
      f'Индекс наибольшего элемента: {max_value[0]}, значение: {max_value[1]}')

# меняем положение максимального и минимального значения
array[min_value[0]], array[max_value[0]] = max_value[1], min_value[1]

print(f'Преобразованный массив: {array}\n')
