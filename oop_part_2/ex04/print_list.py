from node import Node

def print_list(list_head):
    node = list_head.head
    while node != None:
        print(node.content)
        node = node.next
