class linkedList:
    
    def __init__(self, head = None):
        self.head = head
    
    def delete_item_by_value(self,x):
        if not self.head:                 
            pass
        elif self.head.data == x:      
            self.head = self.head.next
        else:
            self.head.remove_node(x)
            return self

class Node:
    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
   
    def remove_node(self, x):
        if not self.next:                    
            pass
        elif self.next.data == x:       
            self.next = self.next.next
        else:
            self.next.remove_node(x)