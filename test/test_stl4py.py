import random
import numpy as np


from stl4py import (count_if,
                    partition,
                    partition_with_pivot,
                    nth_element,
                    unique,
                    minmax_element)


def test_count_if():
    a = range(100)
    assert count_if(a, lambda x: x >= 50) == 50
    assert count_if(a, lambda x: x >= 50, first=0, last=50) == 0
    assert count_if(a, lambda x: x == 0) == 1
    assert count_if(a, lambda x: x % 2 == 0) == len(a) / 2
    assert count_if(a, lambda x: False) == 0
    assert count_if(a, lambda x: True) == len(a)
    a = np.zeros(10, dtype=np.int64)
    assert count_if(a, lambda x: x == 1) == 0
    assert count_if(a, lambda x: x == 0) == 10
    assert count_if(a, lambda x: x) == 0
    a = 'aaabbbccc'
    assert count_if(a, lambda x: x > 'd') == 0
    assert count_if(a, lambda x: x < 'd') == len(a)
    a = [None] * 10
    assert count_if(a, lambda x: x is None) == 10
    a = [1, '1', None, 2, '2', -1, None, 'abc']
    assert count_if(a, lambda x: type(x) == int) == 3
    assert count_if(a, lambda x: x == 'abc') == 1
    assert count_if(a, lambda x: x is None) == 2
    assert count_if(a, lambda x: x == 0) == 0
    a = (1, 2, '3')
    assert count_if(a, lambda x: type(x) == int) == 2
    assert count_if(a, lambda x: type(x) == str) == 1
    assert count_if(a, lambda x: x is not None) == len(a)


def test_partition():
    a = range(100)
    random.shuffle(a)
    f = lambda x: x % 2 == 0
    p_idx = partition(a, f)
    assert all([f(x) for x in a[:p_idx]])
    assert all([not f(x) for x in a[p_idx:]])
    random.shuffle(a)
    a.extend([-1]*50)
    p_idx = partition(a, f, first=0, last=100)
    assert all([f(x) for x in a[:p_idx]])
    assert all([not f(x) for x in a[p_idx:100]])
    assert all([x >= 0 for x in a[:100]])
    assert all([x < 0 for x in a[100:]])
    b = [-1]*50
    b.extend(a)
    p_idx = partition(b, f, first=50, last=150)
    assert all([f(x) for x in b[50:p_idx]])
    assert all([not f(x) for x in b[p_idx:150]])
    assert all([x < 0 for x in b[:50]])
    assert all([x < 0 for x in b[150:]])
    assert all([x >= 0 for x in b[50:150]])
    a = [0]*100
    f = lambda x: x == 0
    p_idx = partition(a, f)
    assert all([f(x) for x in a[:p_idx]])
    assert p_idx == len(a)
    f = lambda x: x != 0
    p_idx = partition(a, f)
    assert p_idx == 0


def test_partition_with_pivot():
    a = range(10)
    for i in range(10):
        random.shuffle(a)
        before_val = a[i]
        pivot_idx = partition_with_pivot(a, i)
        assert before_val == a[pivot_idx]
        assert all([x <= before_val for x in a[:pivot_idx]])
        assert all([x > before_val for x in a[pivot_idx+1:]])
    # check ranges
    for i in range(1, 10):
        for j in range(1, 5):
            a = [999] * i
            b = range(1, 5)
            random.shuffle(b)
            a.extend(b)
            before_val = a[j+i-1]
            pivot_idx = partition_with_pivot(a, j+i-1, first=i)
            assert pivot_idx >= i
            assert all([x == 999 for x in a[:i]])
            assert before_val == a[pivot_idx]
            assert all([x <= before_val for x in a[i:pivot_idx]])
            assert all([x > before_val for x in a[pivot_idx+1:]])
            a = [-1] * i
            b = range(1, 5)
            random.shuffle(b)
            b.extend(a)
            before_val = b[j-1]
            pivot_idx = partition_with_pivot(b, j-1, last=5)
            assert pivot_idx < 5
            assert all([x == -1 for x in b[5:]])
            assert before_val == b[pivot_idx]
            assert all([x <= before_val for x in b[:pivot_idx]])
            assert all([x > before_val for x in b[pivot_idx+1:5]])
    # Check both side ranges
    b = [-1] + range(5) + [-1]
    pivot_idx = partition_with_pivot(b, 1, first=1, last=6)
    assert b[0] == -1
    assert b[-1] == -1
    assert b[1] == 0
    # check key
    a = [(0, 5), (1, 4), (2, 7), (3, 1), (4, 9)]
    pivot_idx = partition_with_pivot(a, 0)
    assert pivot_idx == 0
    pivot_idx = partition_with_pivot(a, 0, key=lambda x: x[1])
    assert pivot_idx == 2


def test_nth_element():
    # TODO: write better tests
    a = range(10)
    for i in range(10):
        random.shuffle(a)
        nth_element(a, i)
        assert a[i] == i
    arr = [4, 1, 2, 3, 3]
    nth_element(arr, 2)
    assert arr[2] == 3, arr
    nth_element(arr, 3)
    assert arr[3] == 3, arr
    arr = [9, 1, 5]
    nth_element(arr, 1)
    assert arr[1] == 5, arr
    arr = [9, 1, 5]
    _key = lambda x: abs(6-x)
    nth_element(arr, 1, key=_key)
    assert arr[1] == 9, arr
    arr = [9, 1, 5]
    nth_element(arr, 1, first=0, last=2)


def test_unique():
    assert unique([]) == []
    assert unique('') == []
    assert unique((),) == []
    assert unique([0]) == [0]
    assert unique('1') == ['1']
    assert unique((2,)) == [2]
    assert unique([1, 2]) == [1, 2]
    assert unique([1, 1, 2]) == [1, 2]
    assert unique([1, 1, 2, 2]) == [1, 2]
    u = unique([2, 4, 6, 1, 3, 5], key=lambda x: x % 2)
    assert u == [2, 1]
    assert unique([1, 1, 1, 3, 4, 5], first=0, last=3) == [1]
    assert unique([1, 1, 1, 3, 4, 5], first=1, last=3) == [1]
    assert unique([1, 1, 1, 3, 4, 5], first=1, last=4) == [1, 3]
    assert unique([1, 1, 1, 3, 4, 5], first=1) == [1, 3, 4, 5]
    assert unique([1, 1, 1, 3, 4, 5], first=3) == [3, 4, 5]


def test_minmax_element():
    a = range(100)
    mn, mx = minmax_element(a)
    assert mn == 0 and mx == 99
    a[55] = -999
    a[33] = 999
    mn, mx = minmax_element(a)
    assert mn == -999 and mx == 999
    a = [(0, 5), (1, 4), (2, 7), (3, 1), (4, 9)]
    mn, mx = minmax_element(a)
    assert mn == (0, 5) and mx == (4, 9)
    mn, mx = minmax_element(a, key=lambda x: x[1])
    assert mn == (3, 1) and mx == (4, 9)
    a = range(100)
    mn, mx = minmax_element(a, first=1)
    assert mn == 1 and mx == 99
    mn, mx = minmax_element(a, last=50)
    assert mn == 0 and mx == 49
    mn, mx = minmax_element(a, first=1, last=50)
    assert mn == 1 and mx == 49
    a = '12345'
    mn, mx = minmax_element(a)
    assert mn == '1' and mx == '5'
    a = (0, 1, 2, 3, 4, 5)
    mn, mx = minmax_element(a)
    assert mn == 0 and mx == 5


def test_partial_sort():
    # TODO: implement
    pass
