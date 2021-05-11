class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def _insert_at_end(self,data):
        if not self.next:
            self.next = Node(data)
        else:
            self.next._insert_at_end(data)

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self,data):
        if not self.head:
            self.head == Node(data)
        else:
            self.head.next._insert_at_end(data)