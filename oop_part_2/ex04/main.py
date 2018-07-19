from node import Node
from merge import merge
from singly_list import SinglyList
from print_list import print_list
from remove import remove

list = SinglyList()

node0 = Node(1)
node1 = Node(5)

node0.next = node1
node1.next = None

anode0 = Node(2)
anode1 = Node(3)

anode0.next = anode1
anode1.next = None

print_list(merge(node0, anode0))
