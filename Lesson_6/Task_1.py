"""
Python 3.9.4 [MSC v.1928 64 bit (AMD64)] on win32

Рассмотрим и проведем исследование затрат памяти
    в 4 задаче 3-го урока(поиск самого частого элемента в массиве)

Метод исследования: рекурсивная функция memory_check написанная на вебинаре
    результаты замеров объектов будем суммировать в глобальные переменные внутри функций
"""
from random import randint
from collections import Counter
import sys


mem_count_1 = 0
mem_count_2 = 0
mem_count_3 = 0


def memory_check(*args):
    """
    Функция из вебинара с рекурсивным вызовом для итерируемых объектов
    Возвращает сумму замеров всего содержимого коллекций
    """
    result = 0
    for el in args:
        result += sys.getsizeof(el)
        if hasattr(el, '__iter__'):
            if hasattr(el, 'items'):
                for key, value in el.items():
                    result += memory_check(key)
                    result += memory_check(value)
            elif not isinstance(el, str):
                for item in el:
                    result += memory_check(item)
    return result


def most_common_original(array):
    """
    Оригинал, как и следует из названия, именно этот код я отправил на проверку
    Расточительно использует память и ресурсы процессора из-за 2 отдельных словарей и циклов for
    """
    global mem_count_1

    num_counter = {}
    result = {'num': 0, 'count': 0}

    for el in array:
        if el in num_counter.keys():
            num_counter[el] += 1
        else:
            num_counter[el] = 1

    for num, count in num_counter.items():
        if result['count'] < count:
            result['num'] = num
            result['count'] = count

    mem_count_1 += memory_check(num_counter)
    mem_count_1 += memory_check(result)
    return result['num']


def most_common_by_counter(array):
    """
    Простая обертка для объекта Counter из модуля collections
    """
    global mem_count_2
    result = Counter(array)

    mem_count_2 += memory_check(result)
    return result.most_common(1)[0][0]


def most_common_single_cycle(array):
    """
    Улучшеный вариант первой функции - использует 1 словарь вместо двух и вычисляет самый частый элемент в том же цикле
    """
    global mem_count_3
    num_counter = {'result': [0, 0]}

    for el in array:
        if el in num_counter.keys():
            num_counter[el] += 1
        else:
            num_counter[el] = 1

        if num_counter[el] > num_counter['result'][1]:
            num_counter['result'] = [el, num_counter[el]]

    mem_count_3 += memory_check(num_counter)
    return num_counter['result'][0]


if __name__ == '__main__':
    """
    При рассмотре результатов работы функций я заметил интересную особенность в работе последней
    в 10-30% случаях результат возврата 3-й функции не совпадал с тем что возвращает 1-я и 2-я
    
    Для того чтобы убедиться что функция работает правильно я написал тест, который сообщит об ошибке в случае если 
    3-я функция вернет элемент который встречается реже чем элемент который возвращают функции 1 и 2
    
    """
    """
    for _ in range(10_000):
        array = [randint(-2000, 2000) for _ in range(1000)]

        call_1 = most_common_original(array)
        call_2 = most_common_by_counter(array)
        call_3 = most_common_single_cycle(array)

        if array.count(call_1) != array.count(call_3) or array.count(call_2) != array.count(call_3):
            print('Функция 3 отработала неправильно, вернула не самый частый элемент из массива, ставьте мне не зачёт')
        assert array.count(call_1) == array.count(call_3)
        assert array.count(call_2) == array.count(call_3)
    """

    # делаем 1000 проходов цикла, генерируя новые входные данные и вызывая наши функции на каждой итерации
    # результаты будут суммироваться в переменные
    for _ in range(1_000):
        array = [randint(-10000, 10000) for _ in range(100)]
        call_1 = most_common_original(array)
        call_2 = most_common_by_counter(array)
        call_3 = most_common_single_cycle(array)

    # делим результаты на 1000 чтобы получить средний
    print(f'Результат замеров потребления памяти с входными данными от -10000 до 10000.\n'
          f'1-я функция: {mem_count_1 // 1_000} байт\n'                                                   # 10_675      
          f'2-я функция: {mem_count_2 // 1_000} байт\n'                                                   # 10_297
          f'3-я функция: {mem_count_3 // 1_000} байт')                                                    # 10_464

    # обнуляем результаты прошлых замеров
    mem_count_1, mem_count_2, mem_count_3 = 0, 0, 0
    print('\n\tПотребление памяти этими функциями напрямую зависит от объема входных данных,'
          'поэтому сделаем еще один замер')

    for _ in range(1_000):
        array = [randint(1, 50) for _ in range(10)]
        call_1 = most_common_original(array)
        call_2 = most_common_by_counter(array)
        call_3 = most_common_single_cycle(array)

    print(f'\nРезультат замеров потребления памяти с входными данными поменьше.\n'
          f'1-я функция: {mem_count_1 // 1_000} байт\n'                                                   # 1267    
          f'2-я функция: {mem_count_2 // 1_000} байт\n'                                                   #  889
          f'3-я функция: {mem_count_3 // 1_000} байт')                                                    # 1167

    """
    Выводы: безусловный фаворит во всех замерах это 2-й вариант с объектом Counter под капотом
    А после нее по эффективности идет 3-й вариант, который я писал специально для этого задания, немного прокачавшись 
    """
