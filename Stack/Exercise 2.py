# Usually stacks are used in for history or for order of operations.

'''
The reason for using deque and not list is because list has to be dynamic
and memory allocation is a problem because it has to copy all the data from previously allocated space
to new space if the allocated space is not enough for the data which might take a lot of time if there
is a lot of data (like millions and billions of data)
'''
from collections import deque

class Stack:
    def __init__(self):
        self.stack_container = deque()

    def push(self, value):
        return self.stack_container.append(value)

    def pop(self):
        return self.stack_container.pop()

    def peek(self):
        return self.stack_container[-1]

    def is_empty(self):
        return len(self.stack_container) == 0

    def size(self):
        return len(self.stack_container)

    def is_match(self, ch1, ch2):
        match_dict = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        return match_dict[ch1] == ch2


    def is_balanced(self, text):
        for char in text:

            if char == '(' or char == '{' or char == '[':
                self.push(char)
            if char == ')' or char == '}' or char == ']':
                if self.size() == 0:
                    return False
                if not self.is_match(char, self.pop()):
                    return False
        return stack.size() == 0


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_balanced("({a+b})"))
    print(stack.is_balanced("))((a+b}{"))
    print(stack.is_balanced("((a+b))"))
    print(stack.is_balanced("((a+g))"))
    print(stack.is_balanced("))"))
    print(stack.is_balanced("[a+b]*(x+2y)*{gg+kk}"))


