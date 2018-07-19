def remove(list_head, val):
    prev = None
    curr = list_head
    while curr:
            if curr.content == val:
                if prev is not None:
                    prev.next = curr.next
                else:
                    while curr.next:
                        curr.content = curr.next.content
                        prev = curr
                        curr = curr.next
                    prev.next = None
                break
            prev = curr
            curr = curr.next
