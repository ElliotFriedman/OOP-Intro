from node import Node
from singly_list import SinglyList

#ordering is incorrect

def merge(train1, train2):
    list_head = SinglyList()
    list_head.add_head(train1)
    train1 = train1.next
    node = list_head.head
    num = 1
    while train1 is not None or train2 is not None:
        if num % 2 == 0 and train1 is not None:
                node.next = train1
                train1 = train1.next
        elif train2 is not None:
            node.next = train2
            train2 = train2.next
        node = node.next
        num += 1
    return list_head
