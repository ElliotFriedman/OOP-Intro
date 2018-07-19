from node import Node
from singly_list import SinglyList

def sort_asc(unsorted_list):
    tmp = unsorted_list.head
    swap = True
    maxv = 0
    tstore = 0
    while swap:
        swap = False
        tmp = unsorted_list.head
        while tmp.next is not None:
            if tmp.content > tmp.next.content:
                tstore = tmp.content
                tmp.content = tmp.next.content
                tmp.next.content = tstore
                swap = True
            tmp = tmp.next

    #swap the first two values
