class Node():
    def __init__(self, value, next = None):
        self.data = value
        self.next = next

class Stack(object):
    
    def __init__(self, node = None):
        self._size = 0
        self.head = node

    def isEmpty(self):
        if self is None:
            return None
        else:
            return False

    def push(self, data):
        n = Node(data)
        n.next = self.head
        self._size += 1
        self.head = n

    def pop(self):
        self.head = self.head.next
        self._size -= 1

    def peek(self):
        if self.head is not None:
            return self.head.data
        return None

    @property
    def size(self):
        return self._size

    def __str__(self):
        tmp = self.head
        _str = "["
        while tmp is not None:
            if tmp.next is not None:
                _str += (str(tmp.data) + ", ")
            else:
                _str += str(tmp.data)
            tmp = tmp.next
        return (_str + "]")
