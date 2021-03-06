"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

numbers = input('Веедите число: ')

even_count, odd_count = 0, 0

for num in numbers:
    if int(num) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f'{even_count} - четных, {odd_count} нечетных')
