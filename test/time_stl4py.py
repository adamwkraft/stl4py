import timeit
import random
import numpy as np

from stl4py import (count_if,
                    partition,
                    partition_with_pivot,
                    nth_element,
                    unique,
                    minmax_element)


SEED = 13531

# TODO: Time different scenarious, like slicing and using a key


def get_random_arrays():
    random.seed(SEED)
    return [[random.randint(0, 100000) for x in range(int(y**2))] for y in np.linspace(10, 500, 50)]


def time_arr_func(func, description):
    print 'Timing:{}'.format(description)
    arrs = get_random_arrays()
    t = timeit.Timer(lambda: func(arrs))
    print t.timeit(10)


def time_x_for_x():
    def f(arrs):
        for a in arrs:
            [x for x in a]
    time_arr_func(f, 'x for x')


def time_sort():
    def f(arrs):
        for a in arrs:
            a.sort()
    time_arr_func(f, 'sort')


def time_sorted():
    def f(arrs):
        for a in arrs:
            sorted(a)
    time_arr_func(f, 'sorted')


def time_count_if():
    def f(arrs):
        for a in arrs:
            count_if(a, lambda x: x == 33)
    time_arr_func(f, 'count_if()')


def time_minmax_element():
    def f(arrs):
        for a in arrs:
            minmax_element(a)
    time_arr_func(f, 'minmax_element()')


def time_unique():
    def f(arrs):
        for a in arrs:
            unique(a)
    time_arr_func(f, 'unique()')


def time_partition():
    def f(arrs):
        for a in arrs:
            partition(a, lambda x: x < 9999)
    time_arr_func(f, 'patition()')


def time_partition_with_pivot():
    def f(arrs):
        for a in arrs:
            partition_with_pivot(a, 99)
    time_arr_func(f, 'partition_with_pivot()')


def time_nth_element():
    def f(arrs):
        for a in arrs:
            nth_element(a, 99)
    time_arr_func(f, 'nth_element()')

if __name__ == '__main__':
    time_x_for_x()
    time_count_if()
    time_minmax_element()
    time_unique()
    time_partition()
    time_partition_with_pivot()
    time_nth_element()
    time_sort()
    time_sorted()
