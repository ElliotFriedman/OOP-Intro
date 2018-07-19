from stack import Stack
from queue import queue

def revKElements(input_string, k):
    _list = input_string
    tmp = _list[:k]
    tmp = tmp[::-1]
    del _list[:k]
    _list = tmp + _list
    print(_list)


_str = input("Enter the list of numbers: ")
_list = _str.replace(" ", "").split(",")

for i in range(len(_list)):
    _list[i] = int(_list[i])

k = int(input("Enter k: "))

revKElements(_list, k)
