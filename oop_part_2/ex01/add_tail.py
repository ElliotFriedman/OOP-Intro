from node import Node

def add_tail(list_head, val):
    if list_head == None:
        list_head = Node(val)
    else:
        node = list_head
        while node.next != None:
            node = node.next
        node.next = Node(val)
