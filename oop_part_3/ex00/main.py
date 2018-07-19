from stack import Node
from stack import Stack

obj = Stack(Node(5))
obj.push(10)
obj.push(12)
obj.push(22)
obj.push(1249)

obj.pop()
print(obj)
print(obj.isEmpty())
print(obj.peek())
print(obj.size)

print()


nobj = Stack()

print(nobj)
print(nobj.isEmpty())
print(nobj.peek())
print(nobj.size)
