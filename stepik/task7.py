class Node:
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None

def PreOrderTraversal(root):
    # NLR
    if (root == None):
        return
    print(root.data, end = " ")
    PreOrderTraversal(root.left)
    PreOrderTraversal(root.right)

def InOrderTraversal(root):
    # LNR
    if (root == None):
        return
    InOrderTraversal(root.left)
    print(root.data, end = " ")
    InOrderTraversal(root.right)

def PostOrderTraversal(root):
    # LRN
    if (root == None):
        return
    PostOrderTraversal(root.left)
    PostOrderTraversal(root.right)
    print(root.data, end = " ")
