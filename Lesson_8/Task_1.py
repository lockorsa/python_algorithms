"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.

Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
"""


def count_substrings(text):
    """считает количество подстрок, добавляя уникальный хэш в множество"""
    res = set()
    for i in range(len(text)):
         for j in range(i + 1, len(text) + 1):
             if text[i:j] != text:
                res.add(hash(text[i:j]))
    res = len(res)
    return res


if __name__ == '__main__':
    print(count_substrings("papa"))
    print(count_substrings("sometexthere")) #73
    print(count_substrings("sova"))
    print(count_substrings("ab"))
