from node import Node
from singly_list import SinglyList
from print_list import print_list
from remove import remove

list = SinglyList()
list.add_head(Node("b"))
list.add_head(Node("c"))
list.add_head(Node("a"))
list.add_head(Node("d"))
list.add_head(Node("e"))
list.add_head(Node("f"))

list_head = list.head

remove(list_head, "a")
print_list(list_head)
