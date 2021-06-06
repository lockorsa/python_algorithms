"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.

Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque


def hex_to_int(number: list):
    DECIMAL = {'0': 0,  '1': 1,
               '2': 2,  '3': 3,
               '4': 4,  '5': 5,
               '6': 6,  '7': 7,
               '8': 8,  '9': 9,
               'A': 10, 'a': 10,
               'B': 11, 'b': 11,
               'C': 12, 'c': 12,
               'D': 13, 'd': 13,
               'E': 14, 'e': 14,
               'F': 15, 'f': 15,}
    start = 1
    result = 0
    for digit in number[::-1]:
        result += DECIMAL[digit] * start
        start *= 16
    return result


def int_to_hex(number: int):
    HEX = {0: '0',
           1: '1',
           2: '2',
           3: '3',
           4: '4',
           5: '5',
           6: '6',
           7: '7',
           8: '8',
           9: '9',
           10: 'A',
           11: 'B',
           12: 'C',
           13: 'D',
           14: 'E',
           15: 'F',}
    result = deque()
    while number > 0:
        result.appendleft(HEX[number % 16])
        number = number // 16
    return list(result)


if __name__ == '__main__':
    assert int_to_hex(hex_to_int('a2') + hex_to_int('c4f')) == ['C', 'F', '1']
    assert int_to_hex(hex_to_int('a2') * hex_to_int('c4f')) == ['7', 'C', '9', 'F', 'E']

    first = [i for i in input('Enter hex number: ')]
    second = [i for i in input('Enter another hex number: ')]
    print(f'Результат сложения - {int_to_hex(hex_to_int(first) + hex_to_int(second))}\n'
          f'Результат произведения - {int_to_hex(hex_to_int(first) * hex_to_int(second))}')
