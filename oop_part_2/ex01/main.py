from node import Node
from singly_list import SinglyList
from print_list import print_list
from add_tail import add_tail

list = SinglyList()
list.add_head(Node("a"))
list.add_head(Node("b"))
list.add_head(Node("c"))
#list.add_head(Node("d"))
#list.add_head(Node("e"))
#list.add_head(Node("f"))
#list.add_head(Node("g"))
add_tail(list.head, "1")

print_list(list.head)
