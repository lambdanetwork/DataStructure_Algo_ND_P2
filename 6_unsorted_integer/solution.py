import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = 0
    max = 0
    for num in ints:
        if(num < min):
            min = num

        if num > max:
            max = num

    return (min, max)
    # Example Test Case of Ten Integers


l = [i for i in range(0, 1000)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 999) == get_min_max(l)) else "Fail")
