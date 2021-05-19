"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
from random import randint


def make_array(min_point, max_point):
    limit = int(input('Введите желаемую длину массива: '))
    return [randint(min_point, max_point + 1) for _ in range(limit)]


print('Передайте параметры массива со случайными числами')
min_point = int(input('Введите нижнюю границу диапозона: '))
max_point = int(input('Введите верхнюю границу диапозона: '))

array = make_array(min_point, max_point)

maximum = {'idx': None, 'value': min_point}
minimum = {'idx': None, 'value': max_point}

for idx, value in enumerate(array):
    if value > maximum['num']:
        maximum['idx'] = idx
        maximum['value'] = value
    elif value < minimum['id']:
        minimum['idx'] = idx
        minimum['value'] = value

print(f'Исходный массив: {array}\n'
      f'Индекс наименьшего элемента: {minimum["idx"]}, значение: {minimum["value"]}\n'
      f'Индекс наибольшего элемента: {maximum["idx"]}, значение: {maximum["value"]}')

# меняем положение максимального и минимального значения
array[minimum['idx']] = maximum['value']
array[maximum['idx']] = minimum['value']

print(f'Преобразованный массив: {array}\n')
