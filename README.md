# stl4py
Python versions of common C++ STL functions


# Introduction
I recently switched from a job coding mostly in C++ to a new job coding in python. This started out as an exercise to translate some functions from the C++ STL that do not seem to be readily available in python. Although some of the functionality of this repo might be useful (or at least allow you to write simpler code), I quickly learned it is very difficult to outperform python built in functions with your own python code.

For example, instead of writing an optimal number of comparison algorithm for minmax_element(), it turns out calling builtin min() and max() is faster. Also with nth_element(), it appears to be quicker to just sort the entire iterable instead of implementing a quick-select algorithm.

There is still more to be done, but I hope this can be the slightest bit of useful to someone.

# Examples

[Unique:](http://en.cppreference.com/w/cpp/algorithm/unique)
```python
import stl4py
a = [1, 1, 2, 3, 1, 1, 4, 4, 5, 5]
unique(a)  # returns [1, 2, 3, 1, 4, 5]
# With ranges
unique(a, first=3, last=7)  # [3, 1, 4]
# With key function
a = [2, 4, 6, 1, 3, 5]
unique(a, key = lambda(x) : x % 2)  # [1, 2]
```
[Partition:](http://en.cppreference.com/w/cpp/algorithm/partition)
```python
import stl4py
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
import stl4py
s = 'Hello, World!'
lower_count = count_if(s, lambda x: x.islower())
print lower_count  # prints 8
a = range(100)
odd_count = count_if(a, lambda x: x % 2 == 0)
print odd_count  # prints 50
```

# Other
Here are other functions available to explore:
* count_if
* partition_with_pivot
* nth_element
* minmax_element
* More to come!
