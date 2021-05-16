class Tree:
    def __init__(self, key=None):
        self.key = key

class Node:
    def __init__(self,key = None ,left = None,right = None):
        self.key = key
        self.left = left
        self.right = right          

def height(node):
    path = 0
    if(node == None):     
        return 0
    while node.right != None or node.left != None:
        while node.right != None:
            node = node.right
            path += 1
        while node.left != None:
            node = node.left
            path += 1
    return path+1                                                       # add 1 for root node

   