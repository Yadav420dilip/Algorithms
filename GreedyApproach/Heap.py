"""A Heap is a complete binary tree-based data structure.

    Max-Heap: The value of each node is less than or equal to the value of the parent. The greatest value is at the
    root. The same property must be true for all subtrees.

    Min-Heap: The value of each node is greater than or equal to the value of its parent. The smallest value is at
    the root. The same property must be true for all subtrees.

    Heaps are used when the highest or lowest order/priority element needs to be removed
    To know the detail about algorithm follow this https://www.youtube.com/watch?v=HqPJF2L5h9U"""

import math


def get_parent(index):
    """Return the parent node index"""
    return math.floor((index - 1) / 2)


def get_greater(children: list):
    """Return greater  value among the children node"""
    if len(children) == 0:
        return None, float('inf')
    if len(children) == 1:
        return children[0]
    else:
        return children[0] if children[0][1] > children[1][1] else children[1]


class MaxHeap:

    def __init__(self, array=None):
        """This is constructor for initializing the variable"""
        if array is None:
            array = []
        self.heapList = array
        self.heapLength = len(self.heapList)

    def get_children(self, index):
        """To get the children in the list, list elements are in tuple format [(child_index, child_node)]"""
        children = []
        child_l = (2 * index) + 1
        child_r = (2 * index) + 2
        if child_l < self.heapLength - 1:
            children.append((child_l, self.heapList[child_l]))

        if child_r < self.heapLength - 1:
            children.append((child_r, self.heapList[child_r]))
        return children

    def push(self, item):
        """Push the element at the end"""
        if self.heapLength == 0:
            self.heapList.append(item)
            self.heapLength += 1
        else:
            self.heapList.append(item)
            self.heapLength += 1
            index = self.heapLength - 1
            self.bubble_up(index)

    def bubble_up(self, index):
        """This is for  adjusting the element after inserting the new element and form the complete tree and
        satisfies the heap condition """
        # print('Heap List', self.heapList)
        # print(index)
        # print(get_parent(index))
        # print("Before", self.heapList[index], self.heapList[get_parent(index)])
        while index > 0 and self.heapList[index] > self.heapList[get_parent(index)]:
            self.heapList[index], self.heapList[get_parent(index)] = self.heapList[get_parent(index)], self.heapList[
                index]
            index = get_parent(index)
            print("After", self.heapList[index], self.heapList[get_parent(index)])

    def pop(self):
        """To remove the element for the 0 index"""
        max_ele = self.heapList.pop(0)
        self.heapLength -= 1
        last = self.heapList.pop(self.heapLength - 1)
        self.heapList.insert(0, last)
        self.bubble_down()
        return max_ele

    def bubble_down(self, index=0):
        """This is for  adjusting the element after deleting the element and form the complete tree and
                satisfies the heap condition """
        children = self.get_children(index)
        # print(children)
        greater_i, greater = get_greater(children)
        while children and self.heapList[index] < greater:
            self.heapList[0], self.heapList[greater_i] = greater, self.heapList[index]
            index = greater_i
            children = self.get_children(index)
            greater, greater_i = get_greater(children)

    def get_heap_lists(self):
        """Return the heap formatted list"""
        return self.heapList

    def enter_the_element(self):
        """This is for entering the element dynamically"""
        while True:
            ele = input('Enter the element->')
            if ele == '':
                break
            else:
                self.push(int(ele))
        return self.get_heap_lists()


"""This is for dynamic input"""
# maxHeap = MaxHeap()
# print(maxHeap.enter_the_element())
# print(maxHeap.get_heap_lists())

"""This is already arrange complete tree"""
# element = [50, 30, 20, 15, 10, 8, 16]
# maxHeap = MaxHeap(element)
# print(maxHeap.get_heap_lists())
# maxHeap.push(60)
# print(maxHeap.get_heap_lists())

"""This is for  remove the greater or topmost element"""
# maxHeap.pop()
# maxHeap.pop()
# print(maxHeap.get_heap_lists())
