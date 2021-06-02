from random import randint
from functools import wraps
import time



def timeit(my_func):
    @wraps(my_func)
    def timed(*args, **kw):
        tstart = time.time()
        output = my_func(*args, **kw)
        tend = time.time()
        print('"{}" took {:.3f} ms to execute\n'.format(my_func.__name__, (tend - tstart) * 1000))
        return output
    return timed


@timeit
def func(array):
    result = [index_ for index_, element in enumerate(array) if not element & 1]
    return result


@timeit
def func_(array):
    result = []
    for index_, element in enumerate(array):
        if not element & 1:
            result.append(index_)
    return result


array = [randint(1, 101) for _ in range(9000)]

print(func(array))
print(func_(array))
