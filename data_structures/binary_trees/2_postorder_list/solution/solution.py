class Node: 
    def __init__(self,key,left=None,right=None): 
        self.left = left
        self.right = right
        self.key = key

def Postorder(root):
    lst = []
    if root:
        lst = Postorder(root.left) 
        lst = lst + Postorder(root.right)
        lst.append(root.key)
    return lst