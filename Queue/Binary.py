
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        return self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return  self.buffer[-1]

    def binary_add(self,n):
        self.enqueue("1")

        for i in range(n):
            front = self.front()
            print(" ", front)
            self.enqueue(front + "0")
            self.enqueue(front + "1")

            self.dequeue()




if __name__ == '__main__':
    pq = Queue()

    pq.binary_add(10)