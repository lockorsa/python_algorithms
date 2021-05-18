"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""

def func(n, tmp = 0, res = 1):
    if n == 0:
        return n / -2
    else:
        tmp = func(n - 1) / -2
        res += tmp
        return res


n = int(input('Введите число: '))

print(func(n))
