from node import Node
from singly_list import SinglyList
from print_list import print_list
from remove import remove
from sort_asc import sort_asc

alist = SinglyList()

node0 = Node(1)
node1 = Node(5)

node0.next = node1

anode0 = Node(2)
anode1 = Node(3)

node1.next = anode0
anode0.next = anode1
anode1.next = None

alist.add_head(node0)

sort_asc(alist)

print_list(alist)
