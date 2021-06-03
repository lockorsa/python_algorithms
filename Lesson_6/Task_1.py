"""

"""
from random import randint
from collections import Counter
import sys


mem_count_1 = 0
mem_count_2 = 0
mem_count_3 = 0


def memory_check(*args):
    result = 0
    for el in args:
        result += sys.getsizeof(el)
        if hasattr(el, '__iter__'):
            if hasattr(el, 'items'):
                for key, value in el.items():
                    result += sys.getsizeof(key)
                    result += sys.getsizeof(value)
            elif not isinstance(el, str):
                for item in el:
                    result += sys.getsizeof(item)
    return result


# функция поиска самого частого элемента
def most_common_original(array):
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
    global mem_count_2
    result = Counter(array)
    mem_count_2 += memory_check(result)
    return result.most_common(1)[0][0]


def most_common_single_cycle(array):
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
    array = [randint(1, 100) for _ in range(10)]

    call_1 = most_common_original(array)
    call_2 = most_common_by_counter(array)
    call_3 = most_common_single_cycle(array)

    print(mem_count_1, mem_count_2, mem_count_3)
