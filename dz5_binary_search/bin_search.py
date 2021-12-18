def bin_search(array, key):
    if len(array) == 0:
        return None
    if len(array) == 1:
        if array[0] == key:
            return 0
        else:
            return None
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound) // 2
        if array[middle] == key:
            n = array.index(key)
            return n
        elif array[middle] > key:
            upper_bound = middle - 1
        elif array[middle] < key:
            lower_bound = middle + 1
    return None

