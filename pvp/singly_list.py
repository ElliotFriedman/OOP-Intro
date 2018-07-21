from node import Node

class SinglyList():
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    @property
    def get_head(self):
        return self.head
    
#    @head.setter
#    def head(self, val):
#        self.head = val
  
    def peek(self):
        return self.get_head().content()

    def createNode(self, data):
        return Node(data)

    def isEmpty(self):
        return self.head == None
    
    def add_head(self, node):
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def add_tail(self, node):
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = node

    def remove_tail(self):
        tmp = self.next
        while tmp.next is not None:
            tmp = tmp.next
        tmp = None

    def remove_head(self):
        tmp = None
        if self.head is not None and self.head.next is not None:
            tmp = self.head.value
            self.head = self.head.next
        elif self.head is not None:
            tmp = self.head.value
            self.head = None
        self._size -= 1
        return tmp
