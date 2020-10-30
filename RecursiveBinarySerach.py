alist = [10, 20, 23, 26, 27, 35, 38, 41, 46, 49, 54, 56, 64, 70, 81, 87, 88, 90, 92, 96, 98]
temp = None


def binary_search(left: int, right: int, key: int) -> int:
    global temp
    if len(alist) == 1:
        if alist[left] == key:
            return alist[left]
        else:
            return 0
    else:
        mid = (left + right) // 2
        print("mid ", mid)
        if mid == temp or mid > len(alist) - 1:  # Condition for preventing the deep recursion.
            return 0
        else:
            temp = mid
            if alist[mid] == key:
                return alist[mid]
            elif key < alist[mid]:
                return binary_search(left, mid - 1, key)
            else:
                return binary_search(mid + 1, right, key)


""" 
This segment for dynamic of the program
"""

# while True:
#     a = input("Enter the element of the list = ")
#     if a == "":
#         break
#     else:
#         alist.append(int(a))


alist.sort()
print(alist)
print(len(alist))
search_key = int(input("Enter the number you want to search  = "))
result = binary_search(0, len(alist), search_key)
print(result)
