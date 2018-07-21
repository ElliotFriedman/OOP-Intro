from node import Node
from queue import Queue
from singly_list import SinglyList


def print_list(singly_list):
    for node in singly_list:
        print(node.content)

n = SinglyList()
n.add_head(Node(1))
n.add_tail(Node(5))
n.add_tail(Node(5))
n.add_tail(Node(5))
n.add_tail(Node(5))
n.add_head(Node(9))
print_list(n)



x = Queue()
x.enqueue(99)
x.enqueue(120)

print(x)


