from has_cycle import has_cycle
from node import Node
from singly_list import SinglyList

list = SinglyList()
#list.add_head(Node("f"))

node0 = Node("a")

node1 = Node("b")
node0.next = node1

#node1.next = node0
node1.next = None

list.add_head(node1)
list_head = list.head

print(has_cycle(list_head))
