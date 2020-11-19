"""Huffman Coding is a technique of compressing data to reduce its size without losing any of the details. It was first developed by David Huffman.

Huffman Coding is generally useful to compress the data in which there are frequently occurring characters."""


class Node:
    """Create the tree node"""
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return '%s %s' % (self.left, self.right)


strings = 'BCAADDDCCACACAC'


def huffman_coding(node, binary_string=''):
    """Implementing the huffman coding"""
    if type(node) is str:
        return {node: binary_string}

    l, r = node.children()
    code = dict()
    code.update(huffman_coding(l, binary_string + '0'))
    code.update(huffman_coding(r, binary_string + '1'))
    return code


def compress_string(code):
    """Compress the string using huffman code"""
    compress_str = ''
    for string in strings:
        compress_str += code[string]
    return compress_str


def decompress_code(nodes, compress_str=None):
    """Decompreess the code using tree node"""
    node_state = nodes
    original_str = ''
    for i in compress_str:
        if i == '0':
            node = node_state.getleft()
        else:
            node = node_state.getright()

        if type(node) is str:
            original_str += node
            node_state = nodes
        else:
            node_state = node

    return original_str


nodes = {i: strings.count(i) for i in strings}# count the alaphabet iteration
nodes = sorted(nodes.items(), key=lambda item: item[1], reverse=True) # sort the dictionary on the basis of value in descending order 

while len(nodes) > 1:
    char1, freq1 = nodes.pop(len(nodes) - 1) #
    char2, freq2 = nodes.pop(len(nodes) - 1)
    new_node = Node(char2, char1)
    nodes.append((new_node, freq1 + freq2))
    nodes.sort(key=lambda item: item[1], reverse=True)

    
huffman_code = huffman_coding(nodes[0][0])

print("Original String --->",strings)
print("String size %s * 8 = %s"%(len(strings), len(strings)*8))

print("Character code table")
print("Char -------> Code ------->  Total")
code_sum, char_sum = 0, 0
for char, code in huffman_code.items():
    code_sum += len(code)
    char_sum += 1
    print('%4s -------> %4s -------> %s * %s = %s' % (char, code, (strings.count(char)), len(code), strings.count(char)*len(code)))

compress_str = compress_string(huffman_code)
print("sum %s*8=%s -------> %s ------->  %s"%(char_sum,(char_sum*8), code_sum, len(compress_str)))
print("Compressed Size is %s"%((char_sum*8)+code_sum+len(compress_str)))
print("compress String --->",compress_str)

decompress_str = decompress_code((nodes[0][0]),compress_str)
print("Decompress String --->",decompress_str)
