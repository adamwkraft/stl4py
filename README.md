# stl4py
Python versions of common C++ STL functions


# Introduction
I recently switched from a job coding mostly in C++ to a new job coding in python. This started out as an exercise to translate some functions from the C++ STL that do not seem to be readily available in python. Although some of the functionality of this repo might be useful (or at least allow you to write simpler code), I quickly learned it is very difficult to outperform python built in functions with your own python code.

For example, instead of writing an optimal number of comparison algorithm for minmax_element(), it turns out calling builtin min() and max() is faster. Also with nth_element(), it appears to be quicker to just sort the entire iterable instead of implementing a quick-select algorithm.

There is still more to be done, but I hope this can be the slightest bit of useful to someone.
