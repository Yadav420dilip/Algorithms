def permutation(list, start, end):
    '''This prints all the permutations of a given list
       it takes the list,the starting and ending indices as input'''
    if start == end:
        print(list)
    else:
        for i in range(start, end + 1):
            list[start], list[i] = list[i], list[start]
            # print("1")# The swapping
            permutation(list, start + 1, end)
            # print("2")
            list[start], list[i] = list[i], list[start]  # Backtracking


permutation([1, 2, 3], 0, 2)  # The first index of a list is zero
