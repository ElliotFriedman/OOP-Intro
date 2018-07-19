from node import Node
from singly_list import SinglyList

#ordering is incorrect

def merge(train1, train2):
    list_head = SinglyList()
    list_head.add_head(Node("Test"))
    node = list_head.head
    num = 0
    while train1 is not None or train2 is not None:
        if num % 2 == 0:
            node.next = train1
            train1 = train1.next
        else:
            node.next = train2
            train2 = train2.next
        node = node.next
        num += 1
    return list_head
