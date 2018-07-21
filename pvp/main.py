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

#create a linked list
n = SinglyList()
n.add_head(Node(1))
n.add_tail(Node(5))
n.add_tail(Node(5))
n.add_tail(Node(5))
n.add_tail(Node(5))
n.add_head(Node(9))
print_list(n)

print("List after removing tail")
n.remove_tail()
print_list(n)
print("List after removing head")
n.remove_head()
print_list(n)

#turn this linked list into a queue
x = Queue(n.head)

#add two more values to this queue
x.enqueue(99)
x.enqueue(120)

#print out queue
while x.isEmpty() == False:
    print()
    print("value dequeued", x.dequeue())
    print()
