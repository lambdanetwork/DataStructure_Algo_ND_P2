def merge(left, right):
    mergedArray = []

    def innerloop():
        if len(left) > 0 and len(right) > 0:
            if(left[0] > right[0]):
                mergedArray.append(left[0])
                left.pop(0)
            else:
                mergedArray.append(right[0])
                right.pop(0)
            innerloop()
        elif len(left) > 0:
            mergedArray.append(left[0])
            left.pop(0)
            innerloop()
        elif len(right) > 0:
            mergedArray.append(right[0])
            right.pop(0)
            innerloop()
    innerloop()
    return mergedArray


def merge_sort(array):
    # sort from big to small
    if len(array) <= 1:
        return array

    middle = int(len(array) / 2)
    Left = array[0:middle]
    Right = array[middle:]

    Left = merge_sort(Left)
    Right = merge_sort(Right)

    return merge(Left, Right)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = merge_sort(input_list)
    answer = ['', '']
    for index, num in enumerate(sorted_list, start=0):
        if index % 2 == 0:  # even index
            answer[0] += str(num)
        else:  # odd index
            answer[1] += str(num)

    answer[0] = int(answer[0])
    answer[1] = int(answer[1])
    return answer


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
