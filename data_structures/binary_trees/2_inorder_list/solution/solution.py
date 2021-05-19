class Node: 
    def __init__(self,key,left=None,right=None): 
        self.left = left
        self.right = right
        self.key = key

def Inorder(root):
    lst = []
    if root:
        lst = Inorder(root.left) 
        lst.append(root.key)
        lst = lst + Inorder(root.right)
    return lst
    #print(lst)

items = Node(5)
#print('Items1 -- > ', items)
items.left = Node(6)
#print('Items2 -- > ', items)
items.right = Node(7)
#print('Items3 -- > ', items)
items.left.left = Node(8)
#print('Items4 -- > ', items)
items.left.right = Node(9)
#print('Items5 -- > ', items)
result_value_1 = Inorder(items)
#print('Items Inorder -- > ', items)

# class Tree:
#     def __init__(self, value=None):
#         self.value = value

#     def __str__(self):
#         root = self.root_node if self.root_node else '<>'
#         return f'<{root}>'

# class Node:
#     def __init__(self,value = None ,left = None,right = None):
#         self.value = value
#         self.left = left
#         self.right = right          

# def Inorder(root):
#         left = f'{Node(root).left}, ' if Node(root).left else ''
#         right = f', {Node(root).right}' if Node(root).right else ''
#         return f'{left}{Node(root).value}{right}'  

