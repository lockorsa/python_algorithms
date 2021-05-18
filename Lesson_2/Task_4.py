"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""

def func(n, result = 1):
    if n == 0:
        return 0
    else:
        result += func(n - 1) / -2
        return result


n = int(input('Введите число: '))

print(func(n))
