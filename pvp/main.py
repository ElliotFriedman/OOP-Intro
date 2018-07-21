from node import Node
from queue import Queue
from singly_list import SinglyList


def print_list(singly_list):
    for node in singly_list:
        print(node.content)

def printn(anode):
    tmp = anode
    while tmp is not None:
        print(tmp.content)
        tmp = tmp.next


n = SinglyList()
n.add_head(Node(1))
n.add_tail(Node(5))
n.add_tail(Node(5))
n.add_tail(Node(5))
n.add_tail(Node(5))
n.add_head(Node(9))


z = n.head
x = Queue(z)
x.enqueue(99)
x.enqueue(120)


while x.isEmpty() == False:
    print()
    print("value dequeued", x.dequeue())
    print()
