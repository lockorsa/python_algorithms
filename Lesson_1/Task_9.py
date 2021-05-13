"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

print('Введите 3 разных числа')

a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))

if a < b and b < c or c < b and b < a:
    print(b)
if b < a and a < c or c < a and a < b:
    print(a)
else:
    print(c)
