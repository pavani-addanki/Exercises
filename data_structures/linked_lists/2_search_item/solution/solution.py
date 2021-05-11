class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def search_node(self, x):
        if not self.next:                    
            return False
        elif self.next.data == x: 
            return True
        else:
            self.next.search_node(x)
            return False

class linkedList:
    def __init__(self, head = None):
        self.head = head

    def search(self,x):
        if not self.head:                 
            return False
        elif self.head.next==None:      
            return True
        else:
            return self.head.search_node(x)
            