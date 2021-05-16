class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next


class linkedList:
    def init(self, head=None):
        self.head = head

    def insert_at_index(self, index, data):
        ind = 1
        n1 = Node(data)
        if self.head == None:
            return None
        else:
            thisvalue = self.head
            print('Head --> ', thisvalue.data)
            while thisvalue.next != None:
                ind += 1
                if ind == index:
                    n1.next = thisvalue.next
                    thisvalue.next = n1
                thisvalue = thisvalue.next

