class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(None, data, self.head)
            self.head = node
            return

        node = Node(None, data, self.head)
        self.head.prev = node
        self.head = node

    def print_forward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next

        print(llstr)


    def print_backward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return

        itr = self.head
        llstr = ''

        while itr.next:
            itr = itr.next

        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.prev

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(None, data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next =  Node(itr, data, None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1

        return count

    def remove_at(self, index):
        if index < 0 or index >= (self.get_length()):
            print("Out of Range")
            #raise Exception("Out of Range")
            return

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                if itr.next is not None:
                    itr.next.prev = itr
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= (self.get_length()):
            print("Out of Range")
            #raise Exception("Out of Range")
            return

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(itr, data, itr.next)
                if itr.next is not None:
                    itr.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            self.insert_at_beginning(data_to_insert)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(itr, data_to_insert, itr.next)
                if itr.next is not None:
                    itr.next.prev = node
                itr.next = node
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            print("Empty Linked List")

        if self.head.data == data:
            self.head.next.prev = None
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                if itr.next is not None:
                    itr.next.prev = itr
                break

            itr = itr.next


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(30)
    ll.insert_at_beginning(40)
    ll.insert_at_end(10)
    ll.insert_values(([10,20,30,40]))
    print("Length of this Linked List is:", ll.get_length())
    ll.print_forward()
    ll.remove_at(2)
    ll.insert_at(2, "hello")
    ll.insert_after_value("hello", 30)
    ll.remove_by_value('hello')
    ll.print_forward()
    ll.print_backward()