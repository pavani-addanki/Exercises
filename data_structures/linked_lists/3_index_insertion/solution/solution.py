class Node:
    def __init__(self, data):        
        self.data = data
        self.next = None
        
class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_index(self,index,data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        elif index > 1:
            current = self.head
            current_index = 1
            while(current is not None):
                current_index += 1
                if(current_index == index):
                    new_node = Node(data)
                    current.next.next = current.next
                    current.next = new_node              
            current = current.next
