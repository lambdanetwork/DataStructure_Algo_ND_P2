import math


def get_next_middle(lower, upper):
    delta = upper - lower
    return int(lower + (delta) / 2)


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number
    low_bound = 0
    high_bound = number

    def loop(num, low, high):
        # if bound is the same as number, just break out of recursive loop
        if low == num or high == num:
            return num

        if num * num == number:
            return num
        elif num * num > number:
            middle = get_next_middle(low, num)
            return loop(middle, low, num)
        else:
            middle = get_next_middle(num, high)
            return loop(middle, num, high)

    ans = loop(int(number / 2), low_bound, high_bound)
    return ans


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (int(math.sqrt(27)) == sqrt(27)) else "Fail")
print("Pass" if (int(math.sqrt(200)) == sqrt(200)) else "Fail")
print("Pass" if (int(math.sqrt(100000000)) == sqrt(100000000)) else "Fail")
print("Pass" if (int(math.sqrt(9999999)) == sqrt(9999999)) else "Fail")
