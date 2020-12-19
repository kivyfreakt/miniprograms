class Node:
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None

def printLevelOrder(root):
    queue = []
    queue.append(root)
    while (queue != []):
        current_node = queue.pop(0)
        if current_node.left != None:
            queue.append(current_node.left)
        if current_node.right != None:
            queue.append(current_node.right)
        print(current_node.data, end = " ")
