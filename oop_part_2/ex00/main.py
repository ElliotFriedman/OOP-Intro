from node import Node
from singly_list import SinglyList
from print_list import print_list

list = SinglyList()
list.add_head(Node("a"))
list.add_head(Node("b"))
list.add_head(Node("c"))
list.add_head(Node("d"))
list.add_head(Node("e"))
list.add_head(Node("f"))
list.add_head(Node("g"))

print_list(list)
