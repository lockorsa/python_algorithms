"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
from random import randint


limit = int(input('Введите желаемую длину массива: '))
array = [randint(1, 101) for _ in range(limit)]

maximum = {'idx': None, 'value': 0}
minimum = {'idx': None, 'value': 100}

for idx, value in enumerate(array):
    if value > maximum['num']:
        maximum['idx'], maximum['value'] = idx, value
    elif value < minimum['id']:
        minimum['idx'], minimum['value'] = idx, value

print(f'Исходный массив: {array}\n'
      f'Индекс наименьшего элемента: {minimum["idx"]}, значение: {minimum["value"]}\n'
      f'Индекс наибольшего элемента: {maximum["idx"]}, значение: {maximum["value"]}')

# меняем положение максимального и минимального значения
array[minimum['idx']] = maximum['value']
array[maximum['idx']] = minimum['value']

print(f'Преобразованный массив: {array}\n')
