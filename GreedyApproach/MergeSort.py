"""Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two
halves and then merges the two sorted halves. """


def merge_sort(values):
    if len(values) > 1:
        mid = len(values) // 2
        left = values[:mid]
        right = values[mid:]
        left = merge_sort(left)
        right = merge_sort(right)


        values = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                values.append(left[0])
                left.pop(0)
            else:
                values.append(right[0])
                right.pop(0)

        for i in left:
            values.append(i)

        for j in right:
            values.append(j)

    return values


items = [13, 12, 11, 13, 31, 5, 6, 7]
items = merge_sort(items)
print(items)
