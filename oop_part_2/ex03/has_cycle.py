def has_cycle(list_head):
    detect = list_head
    node = list_head
    node = node.next
    while node is not None and node != detect:
        node = node.next
    return (node == detect)
