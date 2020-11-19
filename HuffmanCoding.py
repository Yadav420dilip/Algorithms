class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def getleft(self):
        return '%s' % self.left

    def getright(self):
        return '%s' % self.right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return '%s %s' % (self.left, self.right)


strings = 'BCCABBDDAECCBBAEDDCC'


def huffman_coding(node, binary_string=''):
    if type(node) is str:
        return {node: binary_string}

    l, r = node.children()
    code = dict()
    code.update(huffman_coding(l, binary_string + '0'))
    code.update(huffman_coding(r, binary_string + '1'))
    return code


def compress_string(code):
    compress_str = ''
    for string in strings:
        compress_str += code[string]
    return compress_str


def decompress_code(nodes, compress_str=None):
    node_state = nodes
    original_str = ''
    for i in compress_str:
        if i is '0':
            node = node_state.getleft()
        else:
            node = node_state.getright()

        if type(node) is str:
            print(node)
            original_str += node
            node_state = nodes
        else:
            node_state = node

    return original_str


nodes = {i: strings.count(i) for i in strings}
nodes = sorted(nodes.items(), key=lambda item: item[1], reverse=True)

while len(nodes) > 1:
    char1, freq1 = nodes.pop(len(nodes) - 1)
    char2, freq2 = nodes.pop(len(nodes) - 1)
    new_node = Node(char2, char1)
    nodes.append((new_node, freq1 + freq2))
    nodes.sort(key=lambda item: item[1], reverse=True)
print(nodes)
huffman_code = huffman_coding(nodes[0][0])
print("Char -------> Code")
for char, code in huffman_code.items():
    print('%4s -------> %4s' % (char, code))

compress_str = compress_string(huffman_code)
print(compress_str)
print(decompress_code((nodes[0][0]),compress_str))
