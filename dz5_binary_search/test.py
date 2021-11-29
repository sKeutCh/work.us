from random import random

from dz5_binary_search.bin_search import bin_search

assert bin_search([], int(random() * 10**3)) is None, 'error with empty list'

one_length_list = [123]
assert bin_search(one_length_list, 123) == 0, '123 not in list [123]'
assert bin_search(one_length_list, 1) is None, '1 in list [123]'

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # array = list(range(10))
assert bin_search(array, 93) is None, 'error because 93 is not in list'
assert bin_search(array, 5) == 5, 'key index enable is not found'
