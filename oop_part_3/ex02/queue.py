class Node():
    def __init__(self, value, next = None):
        self.data = value
        self.next = next

class queue(object):
    
    def __init__(self, node = None):
        if node is not None:
            self._size = 1
        else:
            self._size = 0
        self.head = node
        

    def isEmpty(self):
        if self is None:
            return None
        else:
            return False

    #go to the end of the list and create a next value
    def enqueue(self, data):
        tmp = self.head
        n = Node(data)
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = n
        n.next = None
        self._size += 1
        

    #set the head to the next node
    def dequeue(self):
        self.head = self.head.next
        self._size -= 1

    def front(self):
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
