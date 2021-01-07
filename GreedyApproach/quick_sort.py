alist = [0, 35, 33, 42, 10, 14, 19, 47, 35, 44, 31, float('inf')]


def partition_function(left, right, pivot):
    left_pointer = left
    right_pointer = right

    while True:
        # print(alist[6])
        # print("Hello ", alist[6] > alist[len(alist)-1])
        while left_pointer < len(alist) and alist[left_pointer] < alist[pivot]:
            left_pointer += 1
            # print('left', left_pointer)

        while right_pointer > 0 and alist[right_pointer] > alist[pivot]:
            # print('right')
            right_pointer -= 1
            # print('right', right_pointer)

        if left_pointer >= right_pointer:
            break
        else:
            # print('swap')
            alist[left_pointer], alist[right_pointer] = alist[right_pointer], alist[left_pointer]
            left_pointer += 1
            right_pointer -= 1
    alist[right_pointer], alist[pivot] = alist[pivot], alist[right_pointer]
    return right_pointer


def quick_sort(left, right):
    if right - left <= 0:
        return
    else:
        pivot = left
        partition = partition_function(left + 1, right, pivot)
        quick_sort(left, partition - 1)
        quick_sort(partition + 1, right)


print('Before \n', alist)
quick_sort(0, len(alist) - 2)
print('After \n', alist)
