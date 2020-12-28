def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    def inner_loop(target, lower_index, upper_index):
        if lower_index == upper_index:
            return -1

        if lower_index < upper_index:
            middle_index = lower_index + int((upper_index - lower_index) / 2)
            if(input_list[middle_index] == target):
                return middle_index
            elif input_list[lower_index] <= input_list[middle_index]:
                if target >= input_list[lower_index] and target < input_list[middle_index]:
                    return inner_loop(target, lower_index, middle_index)
                else:
                    return inner_loop(target, middle_index + 1, upper_index)
            else:
                if target <= input_list[upper_index-1] and target > input_list[middle_index]:
                    return inner_loop(target, middle_index +1, middle_index)
                else:
                    return inner_loop(target, lower_index, middle_index)

    return inner_loop(number, 0, len(input_list))
   

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])