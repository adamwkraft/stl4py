"""
Module containing python-like versions of common C++ STL functions.
"""
import itertools


def count_if(iterable, pred, first=0, last=None):
    """
    Count the number of elements in an iterable that satisfy a condition

    Parameters
    ----------
    iterable: an iterable object with __get_item__
    pred: a unary predicate function
    first: first element to check
    last: one past last element to check. None will check until end of iterable

    Returns
    -------
    count: the number of elements in iterable range that satisfy pred
    """
    assert hasattr(iterable, '__getitem__')
    # Only slice for sub-ranges, slight performance improvement
    iterable = iterable if first == 0 and last is None else iterable[first:last]
    return sum(1 for x in iterable if pred(x))


def partition(iterable, pred, first=0, last=None):
    """
    Parition the iterable from first to last such that all elements
    that satisfy pred are before all elements where pred is false.
    Returns one past the index of the last element where pred is true.
    Relative order of the elements is not preserved.

    Parameters
    ----------
    iterable: a muteable iterable object with __get_item__
    pred: unary boolean predicate function
    first: first element to check
    last: one past last element to check. None will check until end of iterable

    Returns
    -------
    partition_idx: One past last element index where pred is true
    """
    assert hasattr(iterable, '__getitem__')
    last = last or len(iterable)
    assert first <= last
    while first != last:
        # advance first
        while pred(iterable[first]):
            first += 1
            if first == last:
                return first
        # decrement last
        last -= 1
        if first == last:
            return first
        while not pred(iterable[last]):
            last -= 1
            if first == last:
                return first
        # Swap
        iterable[first], iterable[last] = iterable[last], iterable[first]
    return first


def partition_with_pivot(iterable, pivot, first=0, last=None, key=None):
    """
    Partition the iterable from first to last around a given initial pivot,
    such that the resulting order contains elements less than or equal to
    the pivot, the pivot itself, and elements greater than the pivot.
    Returns the new index of the pivot value after partitioning.
    Relative order of the elements is not preserved.

    Parameters
    ----------
    iterable: an iterable object with __get_item__
    pivot: index of the element to use as partition
    first: first element to check
    last: one past last element to check. None will check until end of iterable
    key: function to be called on each list element prior to making comparisons

    Returns
    -------
    result_idx: index of the pivot value after partitioning
    """
    # TODO: use < if there is not key
    assert hasattr(iterable, '__getitem__')
    last = last or len(iterable)
    assert first <= pivot < last
    _cmp = cmp if key is None else lambda x, y: cmp(key(x), y)
    pivot_val = iterable[pivot] if key is None else key(iterable[pivot])
    # Swap pivot to end
    pivot_end_idx = last-1
    iterable[pivot], iterable[last-1] = iterable[last-1], iterable[pivot]
    last -= 1
    while first != last:
        # advance first
        while _cmp(iterable[first], pivot_val) <= 0:
            first += 1
            if first == last:
                iterable[pivot_end_idx], iterable[last] = iterable[last], iterable[pivot_end_idx]
                return last
        # decrement last
        last -= 1
        if first == last:
            iterable[pivot_end_idx], iterable[last] = iterable[last], iterable[pivot_end_idx]
            return last
        while _cmp(iterable[last], pivot_val) > 0:
            last -= 1
            if first == last:
                iterable[pivot_end_idx], iterable[last] = iterable[last], iterable[pivot_end_idx]
                return last
        # Swap
        iterable[first], iterable[last] = iterable[last], iterable[first]
    # Swap pivot into position
    iterable[pivot_end_idx], iterable[last] = iterable[last], iterable[pivot_end_idx]
    return last


def nth_element(iterable, n, first=0, last=None, key=None):
    """
    Partition the iterable from first to last such that the element
    in position n contains the 'nth' element of the iterable in sorted order.
    All elements before the nth element are less than or equal to the
    elements after the new nth element.

    Parameters
    ----------
    iterable: an iterable object with __get_item__
    n: nth element to find
    first: first element to check
    last: one past last element to check. None will check until end of iterable
    key: function to be called on each list element prior to making comparisons
    """
    assert hasattr(iterable, '__getitem__')
    last = last or len(iterable)
    pivot_idx = n
    pivot_idx = partition_with_pivot(iterable, pivot_idx, first=first, last=last, key=key)
    if n == pivot_idx:
        return
    elif n < pivot_idx:
        return nth_element(iterable, n, first, pivot_idx, key=key)
    else:
        return nth_element(iterable, n, pivot_idx+1, last, key=key)


def unique(iterable, first=0, last=None, key=None):
    """
    Returns a list of the elements in iterable, where only the first element
    of repeating consecutive elements is kept. The == operator is used to
    test equality.
    Relative order is preserved.

    Parameters
    ----------
    iterable: an iterable object with __get_item__
    first: first element to check
    last: one past last element to check. None will check until end of iterable
    key: function to be called on each list element prior to checking equality

    Returns
    ------
    result: list of unique elements
    """
    assert hasattr(iterable, '__getitem__')
    last = last or len(iterable)
    assert first <= last
    if first == last:
        return []
    result = [iterable[first]]
    if last - first == 1:
        return result
    iterable = iterable if first == 0 and last is None else iterable[first:last]
    it1, it2 = itertools.tee(iterable, 2)
    next(it2)
    if key is None:
        for x, y in itertools.izip(it1, it2):
            if x != y:
                result.append(y)
    else:
        for x, y in itertools.izip(it1, it2):
            if key(x) != key(y):
                result.append(y)
    return result


def minmax_element(iterable, first=0, last=None, key=None):
    """
    Find and return the minimum and maximum element in an iterable range.

    Parameters
    ----------
    iterable: an iterable object with __get_item__
    first: first element to check
    last: one past last element to check. None will check until end of iterable
    key: function to be called on each list element prior to making comparisons

    Returns
    -------
    min_element, max_element: the resulting minmum and maximum elements
    """
    assert hasattr(iterable, '__getitem__')
    iterable = iterable if first == 0 and last is None else iterable[first:last]
    if key is None:
        return min(iterable), max(iterable)
    else:
        return min(iterable, key=key), max(iterable, key=key)


# TODO: Partial sort
