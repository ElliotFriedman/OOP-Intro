def print_list(list_head):
    node = list_head
    while node != None:
        print(node.content)
        node = node.next
