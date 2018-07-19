from stack import Node
from stack import Stack

def math(_list):
   
    _size = len(_list)
    print("Enter the numbers: ", end="")
    print(str(_list)[1:-1])

    print("Total count =", _size)

    i = 0
    nstack = Stack()
    while i < _size:
        nstack.push(_list[i])
        i += 1
    
    tmp = nstack.head
    total = 0
    while tmp is not None:
        total += tmp.data
        tmp = tmp.next
    print("Sum =", total)

    tmp = nstack.head
    total = 1
    while tmp is not None:
        total *= tmp.data
        tmp = tmp.next
    print("Product =", total)

    tmp = nstack.head
    total = 0
    while tmp is not None:
        total += tmp.data
        tmp = tmp.next
    print("Mean =", (total / _size))

    tmp = nstack.head
    mini = tmp.data
    while tmp is not None:
        if tmp.data < mini:
            mini = tmp.data
        tmp = tmp.next
    print("Min =", mini)

    tmp = nstack.head 
    mini = tmp.data
    while tmp is not None:      
        if tmp.data > mini:
            mini = tmp.data
        tmp = tmp.next
    print("Max =", mini)
