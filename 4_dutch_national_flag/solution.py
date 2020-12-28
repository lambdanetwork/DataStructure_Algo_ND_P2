def get_middle(length):
    if length % 2 == 0:
        return int(length / 2)
    else:
        return int(length / 2) + 1


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    frequency_dict = {
        0: 0,
        1: 0,
        2: 0
    }
    answer = []
    for num in input_list:
        frequency_dict[num] += 1

        if num == 0:
            answer.insert(0, 0)
        elif num == 2:
            answer.append(2)
        else:
            if frequency_dict[2] == 0:
                answer.append(1)
            else:
                # should insert 1 in middle
                length = frequency_dict[0] + \
                    frequency_dict[1] + frequency_dict[2]
                index_for_1 = get_middle(length)

                answer.insert(index_for_1 - 1, 1)
    return answer


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([])
test_function([2, 0, 1])
test_function([0, 1, 2])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
