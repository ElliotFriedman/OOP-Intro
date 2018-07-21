from singly_list import SinglyList

 
class Queue():
    def __init__(self, alist = None):
        #not a node, linked list
        if alist is not None:
            self._size = 1
        else:
            self._size = 0
        self.head = alist

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def enqueue(self, data):
        self.head.add_tail(createNode(data))
        self._size += 1
    
    def dequeue(self):
        return remove_head()
    
    def front(self):
        if self.head.isEmpty() == False:
            return self.peek()
        return None
    
    @property
    def size(self):
        return self._size
    
    def __str__(self):
        tmp = self.head
        _str = []
        i = 0
        while tmp is not None:
            _str.append(str(tmp.peek()))
            tmp = tmp.next
            i += 1
        _str = _str[::-1]
        
        nstr = "["
        i = 0
        while i < len(_str):
            if i + 1 != len(_str):
                nstr += (_str[i] + ", ")
            else:
                nstr += _str[i]
            i += 1
        nstr += "]"
                
        return (nstr)
