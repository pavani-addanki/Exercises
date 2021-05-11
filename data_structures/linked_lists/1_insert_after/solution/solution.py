class Node:
    def __init__(self, data):        
        self.data = data
        self.next = None

    def _insert_after_item(self,x,data):        
        if self.next.data == x:
            self.next.next = Node(data)
        elif self.next.next is not None:
            self.next._insert_after_item(x,data)

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_after_item(self,x,data):
        print(x)
        print(data)
        #x_found = False
        if not self.head:
            self.head = Node(data)
        if(self.head.data == x):
            #if self.head.next == None:
            self.head.next = Node(data)
               # x_found = True
        else:
            print('else')
            self.head._insert_after_item(x,data)
