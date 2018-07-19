from queue import Node
from queue import queue
from stack import Stack

def revKElements(input_string, k):
    i = 0
    s = Stack()
    while input_string.isEmpty() is False and k != 0:
        s.push(input_string.front())
        if input_string.front() is not None:
            input_string.dequeue()
        #print(s, end="")
        #print(input_string)
        k -= 1
        i += 1

    while s.isEmpty() is False:
        #print(s)
        input_string.enqueue(s.peek())
        print(input_string)
        s.pop()

    return input_string

#turn list into a string and then turn each string into an integer
_str = input("Enter the list of numbers: ")
_list = _str.replace(" ", "").split(",")

for i in range(len(_list)):
    _list[i] = int(_list[i])

k = int(input("Enter k: "))

#print(_list)

n = queue(Node(_list[0]))
i = 1 
while i < len(_list):
    n.enqueue(_list[i])
    i += 1

#print(n)

print(revKElements(n, k))
