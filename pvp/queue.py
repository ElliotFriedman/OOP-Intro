from node import Node
 
class Queue():
    def __init__(self, anode = None):
        if anode is not None:
            i = 0
            tmp = anode
            while tmp is not None:
                tmp = tmp.next
                i += 1
            self._size = i
        else:
            self._size = 0
        self.head = anode

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False

    def enqueue(self, data):
        n = Node(data)
        tmp = self.head
        if tmp is not None:
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = n
        elif self.head is None:
            self.head = n
        self._size += 1
    
    def dequeue(self):
        tmp = None
        #print("Removing", self.head.content)
        if self._size > 0:
            #print("there was a value at the head")
            tmp = self.head.content
            self.head = self.head.next
            self._size -= 1
        else:
            print("Can't dequeue an empty queue")
        return tmp
    
    def front(self):
        if self.head.isEmpty() == False:
            return self.peek()
        return None
    
    @property
    def size(self):
        return self._size

    #def __str__(self):
        #finding the start of the singly list
     #   tmp = self.head
      #  _str = []
       # i = 0
        #while tmp is not None:
         #   _str.append(str(tmp.peek()))
          #  tmp = tmp.next
           # i += 1
#        _str = _str[::-1]
        
 #       nstr = "["
  #      i = 0
   #     while i < len(_str):
    #        if i + 1 != len(_str):
     #           nstr += (_str[i] + ", ")
      #      else:
       #         nstr += _str[i]
        #    i += 1
        #nstr += "]"
                
        #return (nstr)
