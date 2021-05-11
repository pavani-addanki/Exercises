class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linkedList:
    def __init__(self, head = None):
        self.head = head

    def get_count(self):
        current = self.head
        count = 0
        while(current is not None):
            count += 1
            current = current.next
        return count