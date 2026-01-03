# All the functions of a Linked List

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_linked_list(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

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
                node = Node(data, itr.next)
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
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            print("Empty Linked List")

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
                
            itr = itr.next

        """
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove_at(count)
                break
            itr = itr.next
            count += 1
         """
if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_at_beginning(6)
    ll.insert_at_beginning(10)
    ll.insert_at_end(5)
    print("Length of this Linked List is:", ll.get_length())
    ll.insert_values([10,12,13,20])
    #ll.remove_at(5)
    #ll.print_linked_list()
    #ll.remove_at(0)
    #ll.print_linked_list()
    ll.insert_at(2,"hello")
    ll.print_linked_list()
    ll.insert_after_value(12, 1)
    ll.print_linked_list()

    ll.remove_by_value(20)
    ll.print_linked_list()




