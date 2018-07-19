from stack import Stack

def isMatch(char1, char2):
    if char1 == "{" and char2 == "}":
        return True
    if char1 == "(" and char2 == ")":
        return True
    if char1 == "[" and char2 == "]":
        return True
    return False

def isBalanced(string):
    n = Stack()
    i = 0
    while i < len(string):
        if string[i] == "(" or string[i] == "{" or string[i] == "[":
            n.push(string[i])
        elif string[i] == ")" or string[i] == "}" or string[i] == "]":
            if n.isEmpty():
               return False
            elif isMatch(n.peek(), string[i]) == False:
                return False
            n.pop()
        i += 1

    if n.isEmpty() is None:
        return True
    return False

_str = input("Enter the sequence of parenthesis: ")
print(isBalanced(_str))
