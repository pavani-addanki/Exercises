class linkedList:
    
    def __init__(self, head=None):
        self.head = head
    
    def __str__(self):
        if self.head:
            return f"< {self.head} >"
        else:
            return "<>"
    
    def reverse(self):
        previous = None
        current = self.head
        while current:                        
            next = current.next             
            current.next = previous         
            previous = current              
            current = next 
        self.head = previous 
        return self
    
class Node:
    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
    def __str__(self):
        if self.next:
            return f"{self.data}, {self.next}"
        else:
            return str(self.data)
