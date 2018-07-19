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
            if tmp.c > tmp.next.c:
                tstore = tmp.content
                tmp.c = tmp.next.c
                tmp.next.c = tstore
                swap = True
            tmp = tmp.next

    #swap the first two values
