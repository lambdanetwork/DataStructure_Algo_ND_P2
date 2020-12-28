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
    if(len(input_list) <= 0):
        raise Exception("Please provide non-empty array")
    
    sorted_list = merge_sort(input_list)
    answer = ['', '']
    for index, num in enumerate(sorted_list, start=0):
        if(type(num) != int):
            raise Exception("Each member of array has to be number")
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


test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_case = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case)

# cannot accept empty array
try:
    test_case = [[],[]]
    test_function(test_case)
except Exception as e:
    print("pass if Execption is raised", e)


# test, make sure that array is only number
try:
    test_case = [['a','b','c'],[]]
    test_function(test_case)
except Exception as e:
    print("pass if Execption is raised", e)

