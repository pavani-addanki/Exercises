class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,head_node = None,tail_node = None):
        self.head_node = head_node
        self.tail_node = tail_node

    def enqueue(self, value):
        new_node = Node(value)
        if not self.tail_node:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.tail_node.next = new_node       
            self.tail_node = new_node

    def __bool__(self):
        if self.head_node:
            return True
        return False  