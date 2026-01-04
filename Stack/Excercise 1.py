
from collections import deque

class Stack:
    def __init__(self):
        self.stack_container = deque()

    def push(self, value):
        return self.stack_container.append(value)

    def reverse_string(self,sentence):
        for i in range(len(sentence) -1, -1, -1):
            self.push(sentence[i])


    def size(self):
        return len(self.stack_container)

    def pop(self):
        return self.stack_container.pop()

    def reverse_string_alternate(self,s):


        for ch in s:
            self.push(ch)

        rstr = ''
        while self.size() != 0:
            rstr += self.pop()

        return rstr

if __name__ == '__main__':
    stack = Stack()

    stack.reverse_string('We will conquere COVID-19')
    print(stack.stack_container)
    #print(stack.reverse_string_alternate('We will conquere COVID-19'))
    my_string = "".join(stack.stack_container)
    print(my_string)

