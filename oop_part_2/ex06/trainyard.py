from node import Node
from singly_list import SinglyList
from print_list import print_list
from sort_asc import sort_asc
from merge import merge
from random import randint

def merge_n_sort(train1, train2):
    n = merge(train1, train2)
    sort_asc(n)
    return n 

l1 = SinglyList()
l1.add_head(Node(-1))
node = l1.head

for i in range(50):
    new = Node(randint(0, 100))
    node.n = new
    node = node.n

l2 = SinglyList()
l2.add_head(Node(-1))
node = l2.head

for i in range(50):
    new = Node(randint(0, 100))
    node.n = new
    node = node.n

print_list(merge_n_sort(l1.head, l2.head))
