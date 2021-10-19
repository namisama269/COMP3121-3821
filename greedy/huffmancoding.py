from queue import PriorityQueue # to get the lowest weight trees

class HuffmanNode:
    def __init__(self, val, char=None):
        self.val = val
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.val < other.val

def merge(node1, node2):
    """
    Create a new root node and update its left and right pointers
    """

    #print(f"merged node1({node1.val}), node2({node2.val})")
    root = HuffmanNode(node1.val + node2.val)
    root.left = node1 
    root.right = node2 
    return root

def printPreorder(root):
    """
    Print preorder traversal of Huffman tree for debugging
    """
    if root is not None:
        print(root.val, root.char)
        printPreorder(root.left)
        printPreorder(root.right)

def huffmanTree(freqs):
    """
    Create a Huffman tree from the dict of frequencies
    """

    # Insert singular nodes for each character into priority queue
    pq = PriorityQueue()
    for char, freq in freqs.items():
        pq.put(HuffmanNode(freq, char))

    # Merge the 2 smallest trees until only 1 is left
    while pq.qsize() > 1: # should return the correct size
        node1 = pq.get()
        node2 = pq.get()
        pq.put(merge(node1, node2))
    
    # The 1 tree left in the pq is the root
    return pq.get()

def huffmanCode(codeDict, root, currCode):
    """
    Traverse the Huffman tree to get the code for each character.
    If going left, append 0 to the current code, if going right,
    append 1.

    Add the (char, code) pair to codeDict.
    """
    if root is None:
        return
    if root.char is not None:
        codeDict[root.char] = currCode

    huffmanCode(codeDict, root.left, currCode + '0')
    huffmanCode(codeDict, root.right, currCode + '1')

def huffman(freqs):
    """
    Given dict of (char, freq) pairs, return dict of (char, code) pairs.
    """

    root = huffmanTree(freqs)
    codes = {}
    huffmanCode(codes, root, "")
    return codes

"""
Testcases
"""

#characters = "abcdefghijklmnopqrstuvwxyz"

test1 = {
    'a': 82,
    'b': 15,
    'c': 28,
    'd': 43,
    'e': 127,
    'f': 22,
    'g': 20,
    'h': 61,
    'i': 70,
    'j': 2,
}
'''
a 82
b 15
c 28  
d 43
e 127
f 22
g 20
h 61
i 70
j 2

'''

if __name__ == "__main__":
    # User input "char freq" until EOF
    print("Enter characters and frequencies: ")
    freqs = {}
    chars = []
    while True:
        try:
            inp = input().split()
        except EOFError:
            break
        freqs[inp[0]] = int(inp[1])
        chars.append(inp[0])

    # Get the huffman codes
    codes = huffman(test1)

    # Print the codes in order
    chars.sort()
    print()
    for char in chars:
        print(f"{char}  {codes[char]}")
