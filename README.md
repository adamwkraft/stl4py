# stl4py
Python versions of common C++ STL functions


# Introduction
I recently switched from a job coding mostly in C++ to a new job coding in python. This project started out as an exercise to translate some functions from the C++ STL that do not seem to be readily available in python. Although some of the functionality of this repo might be useful (or at least allow you to write simpler code), I quickly learned it is very difficult to outperform python built in functions with your own python code.

For example, instead of writing an optimal number of comparison algorithm for minmax_element(), it turns out calling builtin min() and max() is faster. Also with nth_element(), it appears to be quicker to just sort the entire iterable instead of implementing a quick-select algorithm.

There is still more to be done, but I hope this can be the slightest bit of useful to someone.

# Examples

[Nth Element:](https://en.cppreference.com/w/cpp/algorithm/nth_element)
```python
from stl4py import nth_element
arr = [8, 2, 3, 6, 7, 1, 9, 0, 4, 5]  # Shuffled values from 0-9
nth_element(arr, n=6)
# arr is now partitioned, such that the 6th index contains the value
# at that position if the array were fully sorted.
# Also everything before index 6 is less than that value
# and everything after index 6 is greater than that value.
print arr  # One possible output: [0, 2, 3, 4, 1, 5, 6, 8, 7, 9]
```

[Unique:](http://en.cppreference.com/w/cpp/algorithm/unique)
```python
from stl4py import unique
a = [1, 1, 2, 3, 1, 1, 4, 4, 5, 5]
unique(a)  # returns [1, 2, 3, 1, 4, 5]
# With ranges
unique(a, first=3, last=7)  # [3, 1, 4]
# With key function
a = [2, 4, 6, 1, 3, 5]
unique(a, key=lambda(x) : x % 2)  # [2, 1]
```
[Partition:](http://en.cppreference.com/w/cpp/algorithm/partition)
```python
from stl4py import partition_idx
a = range(10)
partition_idx = partition(a, lambda(x) : x % 2 == 0)
print partition_idx  # prints 5
print a  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (technically there are other valid outputs)
# Partition a range
a = range(10)
partition_idx = partition(a, lambda(x) : x % 2 == 0, first=0, last=6)
print partition_idx  # prints 3
print a  # [0, 4, 2, 3, 1, 5, 6, 7, 8, 9]
```
[Count_if:](http://en.cppreference.com/w/cpp/algorithm/count)
```python
from stl4py import count_if
s = 'Hello, World!'
lower_count = count_if(s, lambda x: x.islower())
print lower_count  # prints 8
a = range(100)
odd_count = count_if(a, lambda x: x % 2 == 0)
print odd_count  # prints 50
```

# Other
Here are other functions available to explore:
* partition_with_pivot
* minmax_element
