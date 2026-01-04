from collections import deque
import time
import threading

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

    def order(self):
        orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
        for order in orders:
            self.enqueue(order)
            print("Now ordering ", order)
            time.sleep(0.5)

    def serve(self):
        time.sleep(1)
        while not self.is_empty():
            print("Now serving",self.dequeue())
            time.sleep(2.0)

if __name__ == '__main__':
    pq = Queue()

    print("Without threading")

    t1 = time.time()
    pq.order()
    pq.serve()

    print("Without threading time: " , time.time() - t1)
    print("With threading")

    t2 = time.time()
    order_thread = threading.Thread(target=pq.order)
    serve_thread = threading.Thread(target=pq.serve)

    order_thread.start()
    serve_thread.start()

    order_thread.join()
    serve_thread.join()
    print("Completed in", time.time() - t2)

