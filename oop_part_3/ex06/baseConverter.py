from stack import Stack

def pnum(num):
    l = ["a", "b", "c", "d", "e", "f"]
    if num >= 10:
        print(l[num - 10], end="")
    else:
        print(num, end="")

def baseConverter(decNum, base):
    if base > 16 or base <= 1:
        print("Enter a base less than 16 and more than 1")
        return 0

    n = Stack()
    while decNum != 0:
        n.push(decNum % base)
        decNum = decNum // base

    while n.isEmpty() is not None:
        pnum(n.peek())
        n.pop()
    print()


num = int(input("Enter the decimal number: "))
base = int(input("Enter the base: "))
baseConverter(num, base)

