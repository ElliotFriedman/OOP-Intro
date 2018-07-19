from queue import Node
from queue import queue

obj = queue(Node(5))
obj.enqueue(10)
obj.enqueue(12)
obj.enqueue(22)
obj.enqueue(1249)

#obj.dequeue()
print(obj)
print(obj.isEmpty())
print(obj.front())
print(obj.size)

